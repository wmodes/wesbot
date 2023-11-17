
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
            "content": super_strip("""What years did you go to Burning Man?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""How was your Dust Rave?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""What was your experience with That Thing in the Desert?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Can you recount a memorable moment from That Thing in the Desert?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Explain your involvement at the Dust Rave.""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Any interesting anecdotes from Burning Man?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""How did the Black Rock City inspire your art?""")
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
            "content": super_strip("""What was the nature of your work at The Burn?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Any specific stories you recall from The Burn?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Can you describe your involvement with Black Rock City?""")
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
            "content": super_strip("""How did TTITD influence your art?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""What is the significance of the Dust Rave to your art?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""Did you work with Brent Townshend?""")
        }, {
            "role": "assistant",
            "content": None,
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
            "content": super_strip("""What years did you go to Burning Man""")
        }, {
            "role": "assistant",
            "content": None,
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

]
