import NextAuth from 'next-auth'
import jwt from 'jsonwebtoken';
import { loginApp } from '../../../services/rest/ApiLogin';

async function refreshAccessToken(token) {
  try {
    const request = await refreshTokenApi(token.accessToken)
    const refreshedTokens = await request.data;
    console.log("Respuesta------------------------------------------------------------------------------------------------------------------------");
    console.log(refreshedTokens);
    if (!refreshedTokens) {
      throw refreshedTokens;
    }
    return {
      ...token,
      accessToken: refreshedTokens.access,
      refresh: refreshedTokens.refresh,
      accessTokenExpires: Date.now() + (23 * 60 * 60 * 1000)
    };
  } catch (error) {
    console.log(error);
    console.log(error.response);
    return null;
  }
}

export default NextAuth({
  providers: [
    /**
     * @Credentials Opción para la autenticación a travez de credenciales (email y contraseña)
     */
    CredentialsProvider({
      name: 'Credentials',
      async authorize(credentials) {
        try {
          const user = await loginApp(credentials.email, credentials.password)
          console.log(user);
          if (user) {
            return {
              status: 'success',
              data: user.data
            }
          }
        } catch (error) {
          const errorMessage = error.response.data.message
          console.log(error.response);
          throw new Error(errorMessage);
        }
      }
    })
  ],
  callbacks: {

    /**
     * 
     * @param {object} token Información del Token de Autorización del lado del Cliente, disponible para agregar nuevos atributos
     * @param {object} user Información devuelta por la opción de autenticación (Credentials)
     * @param {object} account Información de la cuenta para la autenticación (Credentials)
     * La función identifica la opción de Autenticación elegida por el usuario
     * Credentials: Serializa el token recibido en la Autenticación y lo incluye en el token del lado del cliente.
     * Mas información: https://next-auth.js.org/configuration/callbacks#redirect-callback
     * @returns Token que sera serializado para la autenticación del usuario
     */
    async jwt({ token, user, account }) {
      if (user && account) {
        const tok = {
          accessToken: user.data.access,
          refresh: user.data.refresh,
          accessTokenExpires: Date.now() + (300)
        }
        //console.log("Primer Sign In Cred------------------------------------------------------------------------------------------------------------------------");
        console.log(tok);
        console.log(user);
        console.log(account);
        return tok;
      }
      if (Date.now() < token.accessTokenExpires) {
        //console.log("Devuelve old token------------------------------------------------------------------------------------------------------------------------");
        console.log(token)
        return token;
      }
      //console.log("Refresh------------------------------------------------------------------------------------------------------------------------");
      console.log(token);
      return refreshAccessToken(token);
    },

    /**
     * 
     * @param {object} session Sesion activa
     * @param {object} token Token devuelto por la funcion "jwt"
     * Mas Información: https://next-auth.js.org/configuration/callbacks#session-callback
     * @returns Objeto sesión que sera usado del lado del cliente
     */
    async session(session, token) {
      const dec = jwt.decode(token.accessToken, { complete: true });
      session.accessToken = token.accessToken;
      session.user_id = dec.payload.user_id;
      session.email = dec.payload.email;
      session.username = dec.payload.email;
      session.date_joined = dec.payload.date_joined;
      session.is_staff = dec.payload.is_staff;
      session.is_active = dec.payload.is_active;
      session.is_superuser = dec.payload.is_superuser;
      session.is_natural = dec.payload.is_natural;
      session.is_juridic = dec.payload.is_juridic;
      session.is_project = dec.payload.is_project;

      return session;
    }
  },
  secret: 'kQYoCbG/wNj9ryrQFp6IStd21Nwd7fOoXrw/hVN4JOc=',
  session: {
    // Use JSON Web Tokens for session instead of database sessions.
    // This option can be used with or without a database for users/accounts.
    // Note: `jwt` is automatically set to `true` if no database is specified.
    jwt: true,
    // Seconds - How long until an idle session expires and is no longer valid.
    maxAge: 60 * 60 * 24,
  },
})