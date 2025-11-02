import streamlit as st
from gtts import gTTS

def gen(data,voice):
    
    
    if voice=='Lisa':
        tts=gTTS(data,'com','en')
    else:
        tts=gTTS(data,'com.au','en')

    tts.save('Audio.mp3')
    
    
st.title('🔊Brisk')
st.markdown('Fast🏃‍♂️ and secure🔒')
val=st.text_area('Enter something...')
voices=['Lisa','Riya']
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
