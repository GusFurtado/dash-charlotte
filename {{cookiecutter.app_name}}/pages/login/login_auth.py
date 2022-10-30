from flask import session



class LoginError(BaseException):
    pass



class LoginAuth:

    def __init__(self, username:str, password:str):
        session['status'] = self._log_user(username, password)


    def _log_user(self, username:str, password:str):
        """Add your authentication system in this method.

        Parameters
        ----------
        username : str
        password : str

        Returns
        -------
        int
            HTTP Status.

        """

        # Placeholder user list
        USERS = {
            'admin': 'admin',
            'guest': 'guest',
        }

        if username not in USERS:
            raise LoginError('User not found') 
        elif USERS[username] != password:
            raise LoginError('Incorrect password')
        else:
            return 200
            


    @staticmethod
    def check_status() -> int:
        """Check current HTTP status.

        Returns
        -------
        int
            - 200: Success
            - 401: Not authenticated
            - 403: Forbidden
        
        """

        if 'status' in session:
            return session['status']
        else:
            return 401
