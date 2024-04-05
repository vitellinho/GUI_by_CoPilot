import streamlit as st

# Titel der Anwendung
st.title('Schön, dass du wieder da bist!')

# Eingabefelder für E-Mail und Passwort
email = st.text_input('E-Mail')
password = st.text_input('Passwort', type='password')

# Anmeldebutton und Logik für die Anmeldung
if st.button('Anmelden'):
    if email and password:  # Überprüfung, ob beide Felder ausgefüllt wurden
        st.success('Du hast dich erfolgreich angemeldet')  # Erfolgsmeldung
    else:
        st.error('Bitte geben Sie E-Mail und Passwort ein')  # Fehlermeldung, falls Felder leer sind