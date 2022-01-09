import speech_recognition as sr
import streamlit as st


if st.button('Record'):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak anything")
        print("Speak anything")
        audio = r.listen(source, phrase_time_limit=5)

    with st.spinner('Thank you ,Your voice will be converted into text shortly'):
        print("Thank you ,Your voice will be converted into text shortly")

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
            st.success(text)
        except:
            print('Sorry could not recognise your voice')
            st.success('Sorry could not recognise your voice')


