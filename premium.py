"""
╔══════════════════════════════════════════════════════════╗
║  premium.py — Modil Premium                              ║
║  Gère: utilisateurs, abonnements, paiements simulés      ║
║  Ajouté proprement sans toucher au backend existant      ║
╚══════════════════════════════════════════════════════════╝
"""
import hashlib, os, secrets
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get('DATABASE_URL', '')

FREE_DAILY_LIMIT   = 10   # Pati gratis pa jou
PREMIUM_PRICE_USD  = 2.0  # $2/mwa
STREAK_BONUS       = {1:0, 3:5, 7:15, 14:30, 30:50}  # Jou -> Bonus pwen

# ── BADGE DEFINITIONS ──────────────────────────────────────────────────────────
BADGES = {
    'first_game':   {'icon':'🎮', 'name_ht':'Premye Jwèt',     'name_fr':'Premier Jeu',        'name_en':'First Game',      'pts':10},
    'streak_3':     {'icon':'🔥', 'name_ht':'Seri 3 Jou',      'name_fr':'Série 3 Jours',      'name_en':'3-Day Streak',    'pts':20},
    'streak_7':     {'icon':'⚡', 'name_ht':'Seri 7 Jou',      'name_fr':'Série 7 Jours',      'name_en':'7-Day Streak',    'pts':50},
    'streak_30':    {'icon':'💎', 'name_ht':'Seri 30 Jou',     'name_fr':'Série 30 Jours',     'name_en':'30-Day Streak',   'pts':200},
    'perfect_easy': {'icon':'⭐', 'name_ht':'Pafè Fasil',      'name_fr':'Parfait Facile',     'name_en':'Perfect Easy',    'pts':15},
    'perfect_hard': {'icon':'🏆', 'name_ht':'Pafè Difisil',    'name_fr':'Parfait Difficile',  'name_en':'Perfect Hard',    'pts':100},
    'speed_demon':  {'icon':'💨', 'name_ht':'Rapid Anpil',     'name_fr':'Super Rapide',       'name_en':'Speed Demon',     'pts':30},
    'century':      {'icon':'💯', 'name_ht':'100 Pati',        'name_fr':'100 Parties',        'name_en':'100 Games',       'pts':150},
    'daily_champ':  {'icon':'📅', 'name_ht':'Chanjman Jounal', 'name_fr':'Champion du Jour',   'name_en':'Daily Champion',  'pts':25},
    'premium_vip':  {'icon':'👑', 'name_ht':'VIP Premium',     'name_fr':'VIP Premium',        'name_en':'Premium VIP',     'pts':500},
}

# ── LEVEL SYSTEM ───────────────────────────────────────────────────────────────
LEVELS = [
    {'level':1,  'name_ht':'Debutant',    'name_fr':'Débutant',     'name_en':'Beginner',    'min_pts':0},
    {'level':2,  'name_ht':'Elèv',        'name_fr':'Élève',        'name_en':'Student',     'min_pts':100},
    {'level':3,  'name_ht':'Konpetan',    'name_fr':'Compétent',    'name_en':'Competent',   'min_pts':300},
    {'level':4,  'name_ht':'Espè',        'name_fr':'Expert',       'name_en':'Expert',      'min_pts':700},
    {'level':5,  'name_ht':'Mèt',         'name_fr':'Maître',       'name_en':'Master',      'min_pts':1500},
    {'level':6,  'name_ht':'Chanpyon',    'name_fr':'Champion',     'name_en':'Champion',    'min_pts':3000},
    {'level':7,  'name_ht':'Lejann',      'name_fr':'Légende',      'name_en':'Legend',      'min_pts':6000},
    {'level':8,  'name_ht':'Jeni',        'name_fr':'Génie',        'name_en':'Genius',      'min_pts':10000},
]

def get_db():
    url = DATABASE_URL
    if url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql://', 1)
    return psycopg2.connect(url, cursor_factory=RealDictCursor)

def init_premium_tables():
    """Kreye nouvo tab yo san touche tab ki egziste yo."""
    conn = get_db(); cur = conn.cursor()

    # Tab itilizatè
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id          SERIAL PRIMARY KEY,
        name        TEXT NOT NULL UNIQUE,
        pass_hash   TEXT,
        is_premium  BOOLEAN DEFAULT FALSE,
        premium_until TEXT,
        total_points INTEGER DEFAULT 0,
        level       INTEGER DEFAULT 1,
        streak_days INTEGER DEFAULT 0,
        last_played TEXT,
        games_played INTEGER DEFAULT 0,
        created_at  TEXT NOT NULL
    )''')

    # Tab abonneman
    cur.execute('''CREATE TABLE IF NOT EXISTS subscriptions (
        id          SERIAL PRIMARY KEY,
        user_name   TEXT NOT NULL,
        plan        TEXT DEFAULT 'monthly',
        amount_usd  REAL DEFAULT 2.0,
        provider    TEXT,      -- digicel, natcom, card, simulated
        phone       TEXT,
        status      TEXT DEFAULT 'active',  -- active, expired, cancelled
        started_at  TEXT NOT NULL,
        expires_at  TEXT NOT NULL,
        created_at  TEXT NOT NULL
    )''')

    # Tab pwen (detay)
    cur.execute('''CREATE TABLE IF NOT EXISTS points_log (
        id          SERIAL PRIMARY KEY,
        user_name   TEXT NOT NULL,
        points      INTEGER NOT NULL,
        reason      TEXT NOT NULL,  -- answer, streak, daily, bonus
        detail      TEXT,
        created_at  TEXT NOT NULL
    )''')

    # Tab badge
    cur.execute('''CREATE TABLE IF NOT EXISTS user_badges (
        id          SERIAL PRIMARY KEY,
        user_name   TEXT NOT NULL,
        badge_id    TEXT NOT NULL,
        earned_at   TEXT NOT NULL,
        UNIQUE(user_name, badge_id)
    )''')

    # Tab defi jounal
    cur.execute('''CREATE TABLE IF NOT EXISTS daily_challenges (
        id          SERIAL PRIMARY KEY,
        challenge_date TEXT NOT NULL UNIQUE,
        category    TEXT NOT NULL,
        difficulty  TEXT NOT NULL,
        bonus_pts   INTEGER DEFAULT 50,
        description_ht TEXT,
        description_fr TEXT,
        description_en TEXT
    )''')

    # Tab konpletasyon defi jounal
    cur.execute('''CREATE TABLE IF NOT EXISTS challenge_completions (
        id          SERIAL PRIMARY KEY,
        user_name   TEXT NOT NULL,
        challenge_date TEXT NOT NULL,
        score       INTEGER,
        completed_at TEXT NOT NULL,
        UNIQUE(user_name, challenge_date)
    )''')

    # Tab rekonpans fin mwa
    cur.execute('''CREATE TABLE IF NOT EXISTS monthly_rewards (
        id          SERIAL PRIMARY KEY,
        month_year  TEXT NOT NULL,   -- ex: "2025-01"
        user_name   TEXT NOT NULL,
        rank        INTEGER NOT NULL,
        reward_type TEXT NOT NULL,   -- credit_mobile, cash, gift
        reward_value TEXT,
        status      TEXT DEFAULT 'pending',
        created_at  TEXT NOT NULL
    )''')

    conn.commit(); cur.close(); conn.close()
    print("✅ Tables premium kreye/verifye!")

# ── USER MANAGEMENT ────────────────────────────────────────────────────────────
def get_or_create_user(name: str) -> dict:
    """Jwenn oswa kreye yon itilizatè."""
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE name=%s', (name,))
    user = cur.fetchone()
    if not user:
        cur.execute('''INSERT INTO users (name, created_at)
            VALUES (%s, %s) RETURNING *''',
            (name, datetime.utcnow().isoformat()))
        user = cur.fetchone()
        conn.commit()
    cur.close(); conn.close()
    return dict(user) if user else {}

def check_premium_status(name: str) -> bool:
    """Verifye si yon itilizatè se premium aktif."""
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT is_premium, premium_until FROM users WHERE name=%s', (name,))
    row = cur.fetchone(); cur.close(); conn.close()
    if not row or not row['is_premium']: return False
    if row['premium_until']:
        try:
            exp = datetime.fromisoformat(row['premium_until'])
            if datetime.utcnow() > exp:
                # Expire otomatikman
                _expire_premium(name)
                return False
        except: pass
    return True

def _expire_premium(name: str):
    conn = get_db(); cur = conn.cursor()
    cur.execute("UPDATE users SET is_premium=FALSE WHERE name=%s", (name,))
    conn.commit(); cur.close(); conn.close()

def check_daily_limit(name: str) -> dict:
    """Verifye limit jounal pou jwè gratis."""
    conn = get_db(); cur = conn.cursor()
    today = datetime.utcnow().date().isoformat()
    # Konte pati jodi a
    cur.execute('''SELECT COUNT(*) as cnt FROM scores
        WHERE name=%s AND played_at::date::text=%s''', (name, today))
    row = cur.fetchone(); cur.close(); conn.close()
    count = row['cnt'] if row else 0
    return {
        'count': count,
        'limit': FREE_DAILY_LIMIT,
        'remaining': max(0, FREE_DAILY_LIMIT - count),
        'exceeded': count >= FREE_DAILY_LIMIT
    }

# ── POINTS SYSTEM ──────────────────────────────────────────────────────────────
def calculate_points(correct: int, total: int, difficulty: str,
                     time_elapsed: int, is_premium: bool) -> dict:
    """Kalkile pwen avèk bonifikasyon."""
    base = {'easy':1, 'medium':2, 'hard':3}.get(difficulty, 1)
    pts = correct * base

    # Bonus vitès (si fini vit)
    avg_time_per_q = time_elapsed / max(total, 1)
    speed_bonus = 0
    if avg_time_per_q < 8:   speed_bonus = int(pts * 0.5)
    elif avg_time_per_q < 12: speed_bonus = int(pts * 0.25)

    # Bonus perfeksyon
    perfect_bonus = int(pts * 0.3) if correct == total else 0

    # Bonus premium (x1.5)
    premium_mult = 1.5 if is_premium else 1.0
    total_pts = int((pts + speed_bonus + perfect_bonus) * premium_mult)

    return {
        'base_pts': pts,
        'speed_bonus': speed_bonus,
        'perfect_bonus': perfect_bonus,
        'premium_multiplier': premium_mult,
        'total': total_pts
    }

def award_points(name: str, points: int, reason: str, detail: str = ''):
    """Ba itilizatè pwen epi mete a jou nivo li."""
    if points <= 0: return
    conn = get_db(); cur = conn.cursor()
    cur.execute('''INSERT INTO points_log (user_name, points, reason, detail, created_at)
        VALUES (%s, %s, %s, %s, %s)''',
        (name, points, reason, detail, datetime.utcnow().isoformat()))
    cur.execute('''UPDATE users SET total_points = total_points + %s
        WHERE name=%s''', (points, name))
    # Mete nivo a jou
    cur.execute('SELECT total_points FROM users WHERE name=%s', (name,))
    row = cur.fetchone()
    if row:
        new_pts = row['total_points']
        new_level = _calc_level(new_pts)
        cur.execute('UPDATE users SET level=%s WHERE name=%s', (new_level, name))
    conn.commit(); cur.close(); conn.close()

def _calc_level(points: int) -> int:
    level = 1
    for l in LEVELS:
        if points >= l['min_pts']: level = l['level']
    return level

def get_level_info(points: int) -> dict:
    current = LEVELS[0]
    next_lv = None
    for i, l in enumerate(LEVELS):
        if points >= l['min_pts']:
            current = l
            next_lv = LEVELS[i+1] if i+1 < len(LEVELS) else None
    progress = 0
    if next_lv:
        range_pts = next_lv['min_pts'] - current['min_pts']
        earned_pts = points - current['min_pts']
        progress = min(100, int(earned_pts / range_pts * 100))
    return {'current': current, 'next': next_lv, 'progress': progress, 'points': points}

# ── STREAK SYSTEM ──────────────────────────────────────────────────────────────
def update_streak(name: str) -> dict:
    """Mete a jou seri jwè a epi retounen bonus pwen."""
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT streak_days, last_played FROM users WHERE name=%s', (name,))
    row = cur.fetchone()
    if not row: cur.close(); conn.close(); return {'streak':0, 'bonus':0, 'new_badge':None}

    today = datetime.utcnow().date()
    last  = None
    if row['last_played']:
        try: last = datetime.fromisoformat(row['last_played']).date()
        except: pass

    streak = row['streak_days'] or 0
    if last == today:
        cur.close(); conn.close()
        return {'streak': streak, 'bonus': 0, 'new_badge': None}
    elif last == today - timedelta(days=1):
        streak += 1
    else:
        streak = 1  # Reyinisyalize

    cur.execute('UPDATE users SET streak_days=%s, last_played=%s WHERE name=%s',
                (streak, today.isoformat(), name))
    conn.commit(); cur.close(); conn.close()

    # Kalkile bonus streak
    bonus = 0
    for days_req, bonus_pts in sorted(STREAK_BONUS.items()):
        if streak >= days_req: bonus = bonus_pts

    # Badge streak
    new_badge = None
    if streak == 3:   new_badge = 'streak_3'
    elif streak == 7: new_badge = 'streak_7'
    elif streak == 30: new_badge = 'streak_30'

    if new_badge: award_badge(name, new_badge)
    if bonus > 0: award_points(name, bonus, 'streak', f'{streak} days streak')

    return {'streak': streak, 'bonus': bonus, 'new_badge': new_badge}

# ── BADGE SYSTEM ───────────────────────────────────────────────────────────────
def award_badge(name: str, badge_id: str) -> bool:
    """Ba yon badge si jwè pa genyen l deja."""
    if badge_id not in BADGES: return False
    conn = get_db(); cur = conn.cursor()
    try:
        cur.execute('''INSERT INTO user_badges (user_name, badge_id, earned_at)
            VALUES (%s, %s, %s)''',
            (name, badge_id, datetime.utcnow().isoformat()))
        conn.commit()
        # Ba pwen pou badge a
        award_points(name, BADGES[badge_id]['pts'], 'badge', badge_id)
        cur.close(); conn.close()
        return True
    except:  # Deja genyen badge sa
        conn.rollback(); cur.close(); conn.close()
        return False

def check_and_award_badges(name: str, correct: int, total: int,
                           difficulty: str, time_elapsed: int, games_count: int):
    """Verifye ak bay tout badge merite yo."""
    earned = []
    # Premye jwèt
    if games_count == 1:
        if award_badge(name, 'first_game'): earned.append('first_game')
    # 100 pati
    if games_count == 100:
        if award_badge(name, 'century'): earned.append('century')
    # Pafè
    if correct == total:
        badge = 'perfect_hard' if difficulty == 'hard' else 'perfect_easy'
        if award_badge(name, badge): earned.append(badge)
    # Rapid
    avg = time_elapsed / max(total, 1)
    if avg < 7 and correct >= total * 0.8:
        if award_badge(name, 'speed_demon'): earned.append('speed_demon')
    return earned

def get_user_badges(name: str) -> list:
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT badge_id, earned_at FROM user_badges WHERE user_name=%s ORDER BY earned_at DESC', (name,))
    rows = cur.fetchall(); cur.close(); conn.close()
    result = []
    for r in rows:
        b = BADGES.get(r['badge_id'], {})
        result.append({**b, 'badge_id': r['badge_id'], 'earned_at': r['earned_at']})
    return result

# ── DAILY CHALLENGE ────────────────────────────────────────────────────────────
def get_or_create_daily_challenge() -> dict:
    """Kreye oswa jwenn defi jounal la."""
    import random
    today = datetime.utcnow().date().isoformat()
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT * FROM daily_challenges WHERE challenge_date=%s', (today,))
    ch = cur.fetchone()
    if not ch:
        cats = ['geo','sci','hist','sport','tech','art','math','food','animals','haiti']
        diffs = ['easy','medium','hard']
        cat  = random.choice(cats)
        diff = random.choice(diffs)
        descs = {
            'ht': f'Defi jounal: {cat.upper()} — {diff}! +50 pwen bonus!',
            'fr': f'Défi du jour: {cat.upper()} — {diff}! +50 pts bonus!',
            'en': f'Daily challenge: {cat.upper()} — {diff}! +50 pts bonus!'
        }
        cur.execute('''INSERT INTO daily_challenges
            (challenge_date, category, difficulty, bonus_pts, description_ht, description_fr, description_en)
            VALUES (%s,%s,%s,50,%s,%s,%s) RETURNING *''',
            (today, cat, diff, descs['ht'], descs['fr'], descs['en']))
        ch = cur.fetchone()
        conn.commit()
    cur.close(); conn.close()
    return dict(ch) if ch else {}

def complete_daily_challenge(name: str, score: int) -> dict:
    """Mak yon defi jounal kòm konplete."""
    today = datetime.utcnow().date().isoformat()
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT * FROM daily_challenges WHERE challenge_date=%s', (today,))
    ch = cur.fetchone()
    if not ch: cur.close(); conn.close(); return {'completed': False}
    try:
        cur.execute('''INSERT INTO challenge_completions
            (user_name, challenge_date, score, completed_at)
            VALUES (%s, %s, %s, %s)''',
            (name, today, score, datetime.utcnow().isoformat()))
        conn.commit()
        award_points(name, ch['bonus_pts'], 'daily_challenge', today)
        award_badge(name, 'daily_champ')
        cur.close(); conn.close()
        return {'completed': True, 'bonus': ch['bonus_pts']}
    except:
        conn.rollback(); cur.close(); conn.close()
        return {'completed': False, 'already': True}

# ── SUBSCRIPTION / PAYMENT (SIMULATION) ───────────────────────────────────────
def simulate_payment(name: str, provider: str, phone: str = '') -> dict:
    """
    Simile yon peman Digicel/Natcom/Kart.
    Nan pwodwiksyon: ranplase ak API reyèl yo.
    """
    import random
    providers = {
        'digicel': {'success_rate': 0.95, 'name': 'Digicel Haiti'},
        'natcom':  {'success_rate': 0.93, 'name': 'Natcom Haiti'},
        'card':    {'success_rate': 0.98, 'name': 'Credit Card'},
        'test':    {'success_rate': 1.00, 'name': 'Test Mode'},
    }
    p = providers.get(provider, providers['test'])
    success = random.random() < p['success_rate']

    if success:
        # Aktive premium pou 30 jou
        now = datetime.utcnow()
        expires = now + timedelta(days=30)
        conn = get_db(); cur = conn.cursor()

        # Kreye oswa mete a jou itilizatè
        cur.execute('SELECT id FROM users WHERE name=%s', (name,))
        if not cur.fetchone():
            cur.execute('INSERT INTO users (name, created_at) VALUES (%s,%s)',
                       (name, now.isoformat()))

        cur.execute('''UPDATE users SET is_premium=TRUE, premium_until=%s WHERE name=%s''',
                   (expires.isoformat(), name))
        cur.execute('''INSERT INTO subscriptions
            (user_name, plan, amount_usd, provider, phone, status, started_at, expires_at, created_at)
            VALUES (%s,'monthly',%s,%s,%s,'active',%s,%s,%s)''',
            (name, PREMIUM_PRICE_USD, provider, phone,
             now.isoformat(), expires.isoformat(), now.isoformat()))
        conn.commit(); cur.close(); conn.close()

        # Badge VIP
        award_badge(name, 'premium_vip')

        return {
            'success': True,
            'provider': p['name'],
            'expires_at': expires.isoformat(),
            'message': f'Abonnman aktive via {p["name"]} — valid jiska {expires.strftime("%d/%m/%Y")}'
        }
    else:
        return {
            'success': False,
            'provider': p['name'],
            'message': f'Peman echwe via {p["name"]}. Eseye ankò.'
        }

# ── MONTHLY REWARDS ────────────────────────────────────────────────────────────
MONTHLY_REWARD_TIERS = {
    1: {'type': 'credit_mobile', 'value': '500 HTG', 'desc_ht': '500 HTG kredi mobil', 'desc_fr': '500 HTG crédit mobile', 'desc_en': '500 HTG mobile credit'},
    2: {'type': 'credit_mobile', 'value': '250 HTG', 'desc_ht': '250 HTG kredi mobil', 'desc_fr': '250 HTG crédit mobile', 'desc_en': '250 HTG mobile credit'},
    3: {'type': 'gift',          'value': 'Badge Espesyal', 'desc_ht': 'Badge Espesyal', 'desc_fr': 'Badge Spécial',        'desc_en': 'Special Badge'},
}

def process_monthly_rewards(month_year: str):
    """
    Pwosese rekonpans fin mwa pou top 3 premium.
    Rele sa chak 1ye mwa (cron job oswa manyèlman).
    """
    conn = get_db(); cur = conn.cursor()
    # Pi bon skor premium yo pou mwa sa
    cur.execute('''
        SELECT s.name, MAX(s.score) as best_score, u.is_premium
        FROM scores s
        JOIN users u ON u.name = s.name
        WHERE s.played_at >= %s AND s.played_at < %s
          AND u.is_premium = TRUE
        GROUP BY s.name, u.is_premium
        ORDER BY best_score DESC
        LIMIT 3
    ''', (f'{month_year}-01', f'{month_year}-32'))
    top3 = cur.fetchall()

    for i, row in enumerate(top3):
        rank = i + 1
        reward = MONTHLY_REWARD_TIERS.get(rank, {})
        cur.execute('''INSERT INTO monthly_rewards
            (month_year, user_name, rank, reward_type, reward_value, status, created_at)
            VALUES (%s,%s,%s,%s,%s,'pending',%s)
            ON CONFLICT DO NOTHING''',
            (month_year, row['name'], rank,
             reward.get('type',''), reward.get('value',''),
             datetime.utcnow().isoformat()))

    conn.commit(); cur.close(); conn.close()
    return {'processed': len(top3)}

def get_premium_leaderboard_monthly() -> list:
    """Leaderboard mansyèl — sèlman premium."""
    conn = get_db(); cur = conn.cursor()
    today = datetime.utcnow()
    month_start = today.replace(day=1).date().isoformat()
    cur.execute('''
        SELECT s.name,
               MAX(s.score) as score,
               SUM(s.correct) as total_correct,
               COUNT(*) as games,
               u.total_points,
               u.level,
               u.streak_days
        FROM scores s
        JOIN users u ON u.name = s.name
        WHERE s.played_at >= %s AND u.is_premium = TRUE
        GROUP BY s.name, u.total_points, u.level, u.streak_days
        ORDER BY score DESC, total_correct DESC
        LIMIT 10
    ''', (month_start,))
    rows = cur.fetchall(); cur.close(); conn.close()
    return [dict(r) for r in rows]

def get_notification(name: str, lang: str = 'ht') -> dict:
    """Retounen notifikasyon pèsonalize pou yon jwè."""
    conn = get_db(); cur = conn.cursor()
    notifs = []

    # Kote nan klasman
    cur.execute('''
        SELECT COUNT(*) + 1 as rank FROM (
            SELECT name, MAX(score) as best
            FROM scores
            WHERE played_at >= (CURRENT_DATE - INTERVAL '30 days')::text
            GROUP BY name
            HAVING MAX(score) > (SELECT MAX(score) FROM scores WHERE name=%s
                                  AND played_at >= (CURRENT_DATE - INTERVAL '30 days')::text)
        ) sub
    ''', (name,))
    row = cur.fetchone()
    rank = row['rank'] if row else 999

    if 1 < rank <= 5:
        msgs = {
            'ht': f'🔥 Ou se #{rank} nan klasman! Jwe plis pou rive #1!',
            'fr': f'🔥 Vous êtes #{rank} au classement! Jouez plus pour atteindre #1!',
            'en': f'🔥 You are #{rank} on the leaderboard! Play more to reach #1!'
        }
        notifs.append({'type': 'rank', 'msg': msgs.get(lang, msgs['en'])})

    # Verifye si gratis epi ankouraje pou premium
    cur.execute('SELECT is_premium FROM users WHERE name=%s', (name,))
    user_row = cur.fetchone()
    if user_row and not user_row['is_premium']:
        msgs = {
            'ht': '👑 Vin Premium pou patisipe nan rekonpans mansyèl la!',
            'fr': '👑 Passez Premium pour participer aux récompenses mensuelles!',
            'en': '👑 Go Premium to participate in monthly rewards!'
        }
        notifs.append({'type': 'upgrade', 'msg': msgs.get(lang, msgs['en'])})

    cur.close(); conn.close()
    return {'notifications': notifs, 'rank': rank}
