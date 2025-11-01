import streamlit as st
import pyttsx3

def gen(data,voice):
    engine=pyttsx3.init()
    sounds=engine.getProperty('voices')
    if voice=='Lisa':
        engine.setProperty('voice',sounds[1].id)
    else:
        engine.setProperty('voice',sounds[0].id)

    engine.save_to_file(data,'Audio.mp3')
    
    engine.runAndWait()
st.title('🔊Brisk')
st.markdown('Fast🏃‍♂️ and secure🔒')
val=st.text_input('Enter something...')
voices=['Lisa','John']
selected = st.selectbox("Choose an voice", voices)
name=st.text_input('Name for your file',value='Brisk.mp3')



if st.button('Send'):
    gen(val,selected)
    if '.mp3' not in name:
        name=name+'.mp3'
    
    with open('Audio.mp3','rb') as f:
        value=f.read()
        st.write('🎉File generated successfully!!🎉')

        st.download_button(label='📥Download',data=value,file_name=name,mime='audio/mpeg')
