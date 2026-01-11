from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

mysql = MySQL()

class User:
    @staticmethod
    def create_user(username, password):
        """Create a new user with hashed password"""
        try:
            hashed_password = generate_password_hash(password)
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    @staticmethod
    def get_by_username(username):
        """Retrieve user by username"""
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            cur.close()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    @staticmethod
    def verify_user(username, password):
        """Verify user credentials"""
        user = User.get_by_username(username)
        if user and check_password_hash(user[2], password):  # user[2] = password field
            return user
        return None

    @staticmethod
    def log_comparison(user_id, image1_path, image2_path, similarity):
        """Log image comparison to history"""
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                """INSERT INTO comparison_history 
                (user_id, image1_path, image2_path, similarity_value) 
                VALUES (%s, %s, %s, %s)""",
                (user_id, image1_path, image2_path, similarity)
            )
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error logging comparison: {e}")
            return False

    @staticmethod
    def get_comparison_history(user_id):
        """Get all comparisons for a user"""
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                """SELECT image1_path, image2_path, similarity_value, compared_at 
                FROM comparison_history 
                WHERE user_id = %s 
                ORDER BY compared_at DESC""",
                (user_id,)
            )
            history = cur.fetchall()
            cur.close()
            return history
        except Exception as e:
            print(f"Error fetching history: {e}")
            return []