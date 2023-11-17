
import sys
sys.path.append('../')
sys.path.append('../../')
from config import SYSTEM_MSGS

sys_content = SYSTEM_MSGS['functions']

DATA = [

{
    "messages": [
        {
            "role": "system",
            "content": sys_content
        }, {
            "role": "user",
            "content": """Can you tell me about art101"""
        }, {
            "role": "assistant",
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
            "content": """Whats art101 like?"""
        }, {
            "role": "assistant",
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
            "content": """I was thinking of taking cmpm 169 in winter"""
        }, {
            "role": "assistant",
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
            "content": """What is CMPM169"""
        }, {
            "role": "assistant",
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
            "content": """Do you teach art 101?"""
        }, {
            "role": "assistant",
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
            "content": """Do you have group projects in CMPM169?"""
        }, {
            "role": "assistant",
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
            "content": """What language do you focus on in programming for the arts?"""
        }, {
            "role": "assistant",
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
            "content": """Who is Benzy?"""
        }, {
            "role": "assistant",
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
            "content": """Was Benzy on the boat with you?"""
        }, {
            "role": "assistant",
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
            "content": """Did you see Benzy and Jeremiah?"""
        }, {
            "role": "assistant",
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
            "content": """Did you see Benzy and Jeremiah?"""
        }, {
            "role": "assistant",
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
            "content": """Can you elaborate on the project with Rico Thunder?"""
        }, {
            "role": "assistant",
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
            "content": """Describe the artistic collaboration with Lanier Sammons."""
        }, {
            "role": "assistant",
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
            "content": """How's your relationship with your dad"""
        }, {
            "role": "assistant",
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
            "content": """What years did you go to Burning Man?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """How was your Dust Rave?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """What was your experience with That Thing in the Desert?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Can you recount a memorable moment from That Thing in the Desert?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Explain your involvement at the Dust Rave."""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Any interesting anecdotes from Burning Man?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """How did the Black Rock City inspire your art?"""
        }, {
            "role": "assistant",
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
            "content": """What was the nature of your work at The Burn?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Any specific stories you recall from The Burn?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Discuss the collective art installation at Black Rock City."""
        }, {
            "role": "assistant",
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
            "content": """Can you describe your involvement with Black Rock City?"""
        }, {
            "role": "assistant",
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
            "content": """How did TTITD influence your art?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """What is the significance of the Dust Rave to your art?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """Tell me about Co-related Space"""
        }, {
            "role": "assistant",
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
            "content": """Who did you work with on Co-related Space?"""
        }, {
            "role": "assistant",
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
            "content": """What's up with Secret History?"""
        }, {
            "role": "assistant",
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
            "content": """Did you work with Brent Townshend?"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """What years did you go to Burning Man"""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
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
            "content": """What is Unavoidable Disaster?"""
        }, {
            "role": "assistant",
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
            "content": """Tell me something about the Black Rock Station at Burning Man."""
        }, {
            "role": "assistant",
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
            "content": """Who collaborated with you on the River Project?"""
        }, {
            "role": "assistant",
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
            "content": """Who were the key members of the station project?"""
        }, {
            "role": "assistant",
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
            "content": """What made the Black Rock Station installation unique?"""
        }, {
            "role": "assistant",
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
            "content": """What kind of narratives were explored at Black Rock Station?"""
        }, {
            "role": "assistant",
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
            "content": """What themes did you explore with FOMOphobia?"""
        }, {
            "role": "assistant",
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
            "content": """Who were the main collaborators for Black Rock Station?"""
        }, {
            "role": "assistant",
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
            "content": """Share your thoughts on \"Unavoidable Disasster\""""
        }, {
            "role": "assistant",
            "function_call": {  
                "name": "lookup_project",
                "arguments": "{\"name\": \"Unavoidable Disaster\"}"
            }
        }
    ]
},

]