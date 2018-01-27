class Auth {
  static authenticateUser(token, email) {
    localStorage.setItem('token', token);
    localStorage.setItem('email', email);
  }

  static isUserAuthenticated() {
    return localStorage.getItem('token') !== null;
  }

  static deauthenticateUser() {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
  }
}

export default Auth;