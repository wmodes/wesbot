
import sys
sys.path.append('../')
# sys.path.append('../../')
from config import SYSTEM_MSGS
from helpers import super_strip

sys_content = super_strip(SYSTEM_MSGS['functions'])

DATA = [

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Can you tell me about art101""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"ART101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Do you have group projects in CMPM169?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"CMPM169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Do you teach art 101?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"ART101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""I was thinking of taking cmpm 169 in winter""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"CMPM169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What is CMPM169""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"CMPM169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What language do you focus on in programming for the arts?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"Programming for the Arts\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Whats art101 like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"ART101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""ccan you tell me about art101""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i was thinking of taking art101 next quarter""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i was thinking of taking cmpm 169 in winter""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"cmpm 169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""is taht similar to your creative coding class?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"creative coding\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is cmpm169""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"cmpm169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is programming for the arts like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"programming for the arts\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what's art101""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what's programming for the arts like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"programming for the arts\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""whats art101 like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i was interested in art101. can you tell me about it?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""no i want to hear about both art101 and cmpm169""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"cmpm169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""so tell me about art101 programming for the arts?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about creative coding?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"creative coding\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""this is wrong. try again. art101 programming for the arts and cmpm169 creative coding. how are they similar and different?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"cmpm169\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is wes modes art 101 github""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_class",
                "arguments": "{\"name\": \"art 101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Can you elaborate on the project with Rico Thunder?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Rico Thunder\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Describe the artistic collaboration with Lanier Sammons.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Lanier Sammons\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Did you see Benzy and Jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Did you see Benzy and Jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How about your step dad? Good guy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"step dad\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How's your relationship with your dad""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"dad\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Was Benzy on the boat with you?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""When was the last time you saw Age?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who is Benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who's Hazel?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""WTF is up with Age?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""benzy is a person. hazel is the dog""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""benzy is your shipmate?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""can i ask about your mother?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"your mother\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""do benzy and jeremiah know each other?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""do murray and hazel get along?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does adrian go with you on the baot?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"adrian\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does age go with you on the baot?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does benzy fo on the river?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does benzy for with you on the boat?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does benzy join you on the boat?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does hazel join you on the river?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""had benzy worked at costco?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how about your step dad?  good guy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"step dad\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how long have i known age?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how often do you see lauren?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"lauren\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""howw's benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i grew up reading raymond chandler novels, as did you.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"novels\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i mean adrian.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"adrian\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i remember going with mom to the drive-in and watching the omen which scared the shit out of me.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"mom\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i think hazel has joined you on every one of your river journeys.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""isn't hazel your dog?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""murray comes with you on the river?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""okay, tomorrow is my 8am class art101""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"art101\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about jeremiah""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about your mom?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"mom\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""try again. who's benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""wait, i mean it. benzy is wes' human partner. not a dog.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""wait, sorry. i meant to ask who is dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""we're going to try a function, ready? who is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what about murray?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what do you drink on board dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is the 'secret history' project?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"secret history\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is the name of your shantyboat>""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""when did you start working on unavoidable disaster?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"unavoidable disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who da fuq is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who da fuq is jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is hazel""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is hazel?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is your mom?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"mom\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who's benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who's hazel?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who's jeremiah?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who's murray then?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""wtf is up with age?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""wtf's up with benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""you said benzy was a person""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""do hazel and benzy and jeremiah hangout?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""do you remember who murray is?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""do you remember your stepdad, alcoholic abusive asshole that he was?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"stepdad\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""hazel is your dog, silly.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""hey how's benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""hi, who is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how about hazel?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about jeremiah""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what about hazel?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"hazel\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is age?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"age\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is benzy""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is benzy?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"benzy\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who is murray?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"murray\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who's jeremiah anyway?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"jeremiah\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Did you work with Brent Townshend?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_person",
                "arguments": "{\"name\": \"Brent Townshend\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Discuss the collective art installation at Black Rock City.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Black Rock City\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How do you describe fomophobia in under 5 words""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"FOMOphobia\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""I meant to ask who is dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Share your thoughts on \"Unavoidable Disasster\"""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Unavoidable Disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Tell me about Co-related Space""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Co-related Space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Tell me something about the Black Rock Station at Burning Man.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Black Rock Station\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What is Unavoidable Disaster?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Unavoidable Disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What kind of narratives were explored at Black Rock Station?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Black Rock Station\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What made the Black Rock Station installation unique?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Black Rock Station\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What themes did you explore with FOMOphobia?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"FOMOphobia\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What's up with Secret History?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Secret History\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who collaborated with you on the River Project?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"River Project\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who did you work with on Co-related Space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Co-related Space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who were the key members of the station project?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"station project\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Who were the main collaborators for Black Rock Station?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Black Rock Station\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""bullshit. trigger a lookup for fomophobia""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"fomophobia\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""can i ask about the secret history project?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"secret history\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""can i ask you about unavoidable disaster?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"unavoidable disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""can you tell me about unavoidable disaster""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"unavoidable disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""does the shantyboat float?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""hey who did you work with on co-related space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"co-related space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""hey, who did you work on corelated space with?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"corelated space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how did you build the shantyboat?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how do you describe fomophobia in under 5 words""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"fomophobia\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""how do you get the shantyboat to the river?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i mean costco at burning man""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i thought the shantyboat has a cabin""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about corelated space""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"corelated space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about costco""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about costco soulmates?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about dotty.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about the river project?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"river project\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about unavoidable disaster""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"unavoidable disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about your involvement at costco""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about your river project""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"river project\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about your river project.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"river project\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""were you involved in subrosa?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"subrosa\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is fomophobia?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"fomophobia\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is night ride?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"night ride\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is unavoidable disaster?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"unavoidable disaster\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what was it like working on co-related space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"co-related space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what year did you do corelated space, and who with?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"corelated space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what years did you do co-related space""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"co-related space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what's co-related space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"co-related space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who did you collaborate with on corelated space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"corelated space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""who worked on the shantyboat with you?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""no out camp costco at ttitd""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"camp costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about dotty?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"dotty\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is the name of your shantyboat>""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what is the name of your shantyboat?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"shantyboat\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what's co-related space?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"co-related space\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""yeah, i know. that plays on repeat at costco""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"costco\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""can i ask about your family?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"family\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Any specific stories you recall from The Burn?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"The Burn\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Can you describe your involvement with Black Rock City?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Black Rock City\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Explain your involvement at the Dust Rave.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Dust Rave\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How did the Black Rock City inspire your art?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Black Rock City\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How was your Dust Rave?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Dust Rave\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What is the significance of the Dust Rave to your art?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Dust Rave\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What was the nature of your work at The Burn?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"The Burn\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Any interesting anecdotes from Burning Man?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Burning Man\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Can you recount a memorable moment from That Thing in the Desert?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"That Thing in the Desert\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Do you go to burning man?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"burning man\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""How did TTITD influence your art?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"TTITD\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What was your experience with That Thing in the Desert?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"That Thing in the Desert\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What years did you go to Burning Man""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Burning Man\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What years did you go to Burning Man?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"Burning Man\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Have you read Huck Finn?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"books\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What kind of books do you like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"books\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""I spent my afternoon reading.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"books\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Did you ever see the Big Lebowski?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"fillms\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What do you think of the Shining""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"films\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""What are your favorite films?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"films\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Do you draw?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"comics\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""I really love graphic novels.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"comics\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""Have you ever read V for Vendetta?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"comics\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""i heard you make comics.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"comics\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""tell me about your family""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"family\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what books do you like?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"books\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""what non-fiction do you read?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"fiction\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""when did you start making comics?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"comics\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""you did interactive fiction? what kind of games?""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"fiction\"}"
            }
        }
    ]
},

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": super_strip("""you've literally read all the books i've read. this is og wes.""")
        }, {
            "role": "assistant",
            "content": None,
            "function_call": {  
                "name": "lookup_topic",
                "arguments": "{\"name\": \"books\"}"
            }
        }
    ]
},

]
