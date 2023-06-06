
import speech_recognition as sr
import streamlit as st
from st_custom_components import st_audiorec
import string
from itertools import count
from PIL import Image
import os
import time
import numpy as np
import base64

st.set_page_config(page_title="Speech to sign translator")
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)  # remove streamlit header
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)  # adjust height of audio recorder
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # adjust color of links
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # adjust color of links


def speechtosign():

    # TITLE and Creator information
    st.markdown('# Speech-to-Sign-language-Translator')
    st.markdown('Implemented by Rajat Singh')
    st.write('\n\n')
    image_pos = st.empty()
    # a_pos = st.empty()

    # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
    # by calling this function an instance of the audio recorder is created
    # once a recording is completed, audio data will be saved to wav_audio_data
    j = st.button('Say Something', key='1')

    if j:
        r = sr.Recognizer()
        isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                   'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                   'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                   'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                   'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing',
                   'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                   'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                   'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                   'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                   'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                   'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                   'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                   'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
                   'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
                   'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
                   'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
                   'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
                   'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
                   'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
                   'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy']
        arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            i = 0
            while True:
                st.write('I am listening ...')
                print("I am Listening")
                hj = st.button('Stop', key=time.time())

                if hj:
                    break
                audio = r.listen(source)
                # try:
                # text = r.recognize_google(audio)
                # print("You said : {}".format(text))

                try:
                    a = r.recognize_google(audio)
                    a = a.lower()
                    print('You Said: ' + a.lower())
                    st.text('You Said: ' + a.lower())

                    for c in string.punctuation:
                        a = a.replace(c, "")

                    if(a.lower() == 'goodbye' or a.lower() == 'good bye' or a.lower() == 'bye'):
                        print("oops!Time To say good bye")
                        break

                    elif(a.lower() in isl_gif):
                        class ImageLabel(tk.Label):
                            """a label that displays images, and plays them if they are gifs"""

                            def load(self, im):
                                if isinstance(im, str):
                                    im = Image.open(im)
                                self.loc = 0
                                self.frames = []

                                try:
                                    for i in count(1):
                                        self.frames.append(
                                            ImageTk.PhotoImage(im.copy()))
                                        im.seek(i)
                                except EOFError:
                                    pass

                                try:
                                    self.delay = im.info['duration']
                                except:
                                    self.delay = 100

                                if len(self.frames) == 1:
                                    self.config(image=self.frames[0])
                                else:
                                    self.next_frame()

                            def unload(self):
                                self.config(image=None)
                                self.frames = None

                            def next_frame(self):
                                if self.frames:
                                    self.loc += 1
                                    self.loc %= len(self.frames)
                                    self.config(image=self.frames[self.loc])
                                    self.after(self.delay, self.next_frame)
                        # root = tk.Tk()
                        # lbl = ImageLabel(root)
                        # lbl.pack()
                        # lbl.load(r'ISL_Gifs/{0}.gif'.format(a.lower()))
                        # ImageItself = Image.open(
                            # r'ISL_Gifs/{0}.gif'.format(a.lower()))
                        # image_pos.image(ImageItself, width=500)

                        try:
                            try:
                                file_ = open(
                                    r'ISL_Gifs/{0}.gif'.format("hello"), "rb")
                                # print(file_)
                                contents = file_.read()
                                # print(contents)
                                data_url = base64.b64encode(
                                    contents).decode("utf-8")
                                # print(data_url)
                                # file_.close()
                            except:
                                st.text(
                                    "Something went wrong with the gif opening")

                        # image_pos.markdown(
                        #     f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
                        #     unsafe_allow_html=True,
                        # )
                            try:
                                # rt = a_pos.button('Continue', key=time.time())
                                # while True:
                                # print("hello, i came here")
                                image_pos.markdown(
                                    f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
                                    unsafe_allow_html=True,
                                )
                                time.sleep(6)
                                # print("hello, i came here aswell")
                                # image_pos.image(
                                # image='ISL_Gifs/{0}.gif'.format(a.lower()), width=500)
                                # time.sleep(3)

                                image_pos.empty()
                                a_pos.empty()
                            except:
                                st.text(
                                    "Something went wrong with the gif showing")
                        except:
                            st.write(
                                "Something went wrong with the gif system")

                        # root.mainloop()
                    else:
                        for i in range(len(a)):
                            if(a[i] in arr):

                                ImageAddress = 'letters/'+a[i]+'.jpg'
                                ImageItself = Image.open(ImageAddress)
                                image_pos.image(ImageItself, width=500)
                                time.sleep(2)
                                image_pos.empty()
                                # ImageNumpyFormat = np.asarray(ImageItself)
                                # plt.imshow(ImageNumpyFormat)
                                # plt.draw()
                                # plt.pause(0.8)
                            else:
                                continue
                except:
                    st.write("Sorry could not recognize what you said")
    else:
        st.write('Goodbye')
    # wav_audio_data = st_audiorec()  # tadaaaa! yes, that's it! :D

    # add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.markdown(
            """

**An application which takes in live speech or audio recording as input, converts it into text and displays the relevant Indian Sign Language images or GIFs.**
- Front-end using EasyGui.
- Speech as input through microphone using PyAudio. 
- Speech recognition using Google Speech API and Sphix(for offline use).
- Text Preprocessing using NLP.
- Dictionary based Machine Translation.

## To run the application.
1. Open the Downloads folder and then open the terminal.
2. From the terminal, run the *main* python file using the command **python main.py**.
3. The application interface appears on the screen.
4. Hit the record button to start taking speech as input.
5. Any speech recorded is then processed and respective outputs are shown accordingly.
6. To exit the application using speech, say *goodbye*.


**Sign language is a visual language that is used by deaf people as their mother tongue. Unlike acoustically conveyed sound patterns, sign language uses body language and manual communication to fluidly convey the thoughts of a person. Due to considerable time required in learning the Sign Language,  it becomes difficult to communicate with these specially abled people, and thus creates a communication gap.**

## Objective
**This Audio to Sign Language converter aims at :**
- Providing information access and services to deaf people in Indian sign language.
- Developing a scalable project which can be extended to capture whole vocabulary of ISL through manual and non-manual signs

It can be developed as a desktop or mobile application to enable specially abled people to communicate easily and effectively with others

**Sign language is a visual language that is used by deaf people as their mother tongue. Unlike acoustically conveyed sound patterns, sign language uses body language and manual communication to fluidly convey the thoughts of a person. Due to considerable time required in learning the Sign Language, people find it difficult to communicate with these specially abled people, creating a communication gap. Thus, we propose an application which takes in live speech or audio recording as input, converts it into text and displays the relevant Indian Sign Language images or GIFs.**

## Algorithm
Audio to Sign Language Translator
1. Start
2. Getting the Speech
   1. Listen for 1 second and calibrate the energy threshold for ambient noise
levels.
   2. Listen the Speech using Microphone.
Now the energy threshold is already set to a good value, and we can
reliably catch speech right away.
3. Recognise the Speech.
4. Convert Speech to Text.
   1. Make the Text to lowercase for further manipulation.
5. Detected Text
   1. If “goodbye” then exit.
   2.Else if Detected Text in predefined Dictionary Words. Display
respective GIFs of the Phrase.
   3. Else Count the Letters of the Word/Phrase.
      1. Display the Visual of the phrase with some delay of Actions.
   4. Continue all the steps from Step 3, and continue till the Speech Ends.
6. If Error in Step 2, That is if no Speech Detected then display error message
“Could not listen”.

**Due to considerable time required in learning the Sign Language, people find it difficult to communicate with these specially abled people, creating a communication gap. Thus the Audio to Sign Language converter is important and significant because it helps in providing information access and services to deaf people in Indian sign language and develops a scalable project which can be extended to capture whole vocabulary of ISL through manual and non-manual signs. It also can be developed as a desktop or mobile application to enable specially abled people to communicate easily and effectively with others.**

The project before enhancement and modification was cloned from <a href = "https://github.com/Shubh-Yadav/Automatic-Indian-Sign-Language-Translator">Shubh-Yadav</a>
This project is now modified for better and enhanced speech recognition. Also added the program to work in offline mode.

            """, unsafe_allow_html=True
        )

    # if wav_audio_data is not None:
    #     # display audio data as received on the Python side
    #     col_playback, col_space = st.columns([0.58, 0.42])
    #     with col_playback:
    #         st.audio(wav_audio_data, format='audio/wav')


if __name__ == '__main__':
    # call main function
    speechtosign()
