import pyttsx3 as john  # python text to speech package
import openai  # opeanai package

while True:
    def chatgptOutput(inputData):
        OPENAI_API_KEY = ""
        openai.api_key = OPENAI_API_KEY
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=inputData,
            temperature=0.3,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        print(response["choices"][0]["text"])  # Print the output

        A = (response["choices"][0]["text"])  # set the variable name

        def voiceSpeechJohn(A):

            # initialise the pyttsx3 as john
            textSpeech = john.init()

            # getting details of current voicesdfsdfsf adf
            voices = textSpeech.getProperty('voices')

            # change the voice 0 for amle & 1 for female
            textSpeech.setProperty('voice', voices[0].id)

            # say
            textSpeech.say("Hi sir \n i'm your Assistent john")
            textSpeech.say("Ok sir... A simple answer to what you ask")
            textSpeech.say(A)
            # Run the textSpeech
            return textSpeech.runAndWait()
        voiceSpeechJohn(A)
        
    inputData = str(input("What Do You Want: "))  # get the input
    chatgptOutput(inputData)  # call the function
