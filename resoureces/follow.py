from flask_restful import Resource
from flask import request
from mysql_connection import get_connection
from mysql.connector import Error
import mysql.connector
from email_validator import validate_email, EmailNotValidError

from utils import check_password, hash_password 

from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required

import datetime


class FollowResource(Resource):
    @jwt_required()
    def post(self, followee_id):

        user_id = get_jwt_identity()

        try :
            connection = get_connection()
            query = '''
            insert into follow
            (followerId, followeeId)
            values
            (%s, %s);'''
            record = (user_id, followee_id)
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()

            cursor.close()
            connection.close()
        except Error as e:
            print(e)
            return{'result' : 'fail', 'error' : str(e)}, 500

        return {'result': 'success'}
    @jwt_required()
    def delete(self , followee_id):
        user_id = get_jwt_identity()

        try :
            connection = get_connection()
            query = '''
                    delete from follow
                    where followerId = %s and followeeId = %s;
                    '''
            record = (user_id, followee_id)
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()

            cursor.close()
            connection.close()
        except Error as e:
            print(e)
            return{'result' : 'fail', 'error' : str(e)}, 500





