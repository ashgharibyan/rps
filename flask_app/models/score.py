from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Score:
    def __init__(self, data):
        self.id = data['id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.wins = data['wins']
        self.losses = data['losses']
        self.ties = data['ties']
        self.rock = data['rock']
        self.paper = data['paper']
        self.scissor = data['scissor']
        self.user_id = data['user_id']
        self.player = user.User.get_by_id({'id':self.user_id})

# ===================== CREATE A NEW SCORE
    @classmethod
    def create(cls, data):
        query = '''
            INSERT INTO scores (wins, losses, ties, rock, paper, scissor, user_id)
            VALUES (0,0,0,0,0,0,%(user_id)s);
        '''
        
        return connectToMySQL(DATABASE).query_db(query, data)


# ===================== RETURNING LIST OF ALL SCORES
    @classmethod
    def get_all(cls):
        query = '''
            SELECT *
            FROM scores
            JOIN users
            ON users.id=scores.user_id;
        '''
        results = connectToMySQL(DATABASE).query_db(query)    
        all_scores = []
        if results:
            for row in results:
                all_scores.append(cls(row))
        return all_scores

# ===================== RETURNING SCORE BY ID
    @classmethod
    def get_by_id(cls, data):
        query = '''
            SELECT *
            FROM scores
            WHERE id = %(id)s;
        '''
        
        results =  connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])

# ===================== RETURNING SCORE BY USER ID
    @classmethod
    def get_by_user_id(cls, data):
        query = '''
            SELECT *
            FROM scores
            WHERE user_id = %(user_id)s;
        '''
        
        results =  connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])

# ==================== UPDATE WINS
    @classmethod
    def update_wins(cls, data):
        query = '''
            UPDATE scores
            SET wins = wins+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ==================== UPDATE LOSSES
    @classmethod
    def update_losses(cls, data):
        query = '''
            UPDATE scores
            SET losses = losses+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ==================== UPDATE TIES
    @classmethod
    def update_ties(cls, data):
        query = '''
            UPDATE scores
            SET ties = ties+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ==================== UPDATE ROCK
    @classmethod
    def update_rock(cls, data):
        query = '''
            UPDATE scores
            SET rock = rock+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ==================== UPDATE PAPER
    @classmethod
    def update_paper(cls, data):
        query = '''
            UPDATE scores
            SET paper = paper+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ==================== UPDATE SCISSOR
    @classmethod
    def update_scissor(cls, data):
        query = '''
            UPDATE scores
            SET scissor = scissor+1
            WHERE user_id = %(user_id)s;
        '''

        return connectToMySQL(DATABASE).query_db(query, data)

# ===================== RETURNING SCOREBOARD DESC ORDER
    @classmethod
    def scoreboard(cls):
        query = '''
            SELECT username, wins, losses, ties, rock, paper, scissor FROM scores
            JOIN users
            ON users.id=scores.user_id
            ORDER BY wins DESC;
        '''
        
        results =  connectToMySQL(DATABASE).query_db(query)
        if len(results) < 1 :
            return []
        return results