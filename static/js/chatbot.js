/*
   chatbot.js - A JavaScript file for implementing a chatbot.

   This file contains the code for handling user input, sending requests to a chatbot API, 
   storing and displaying the chat, and other related functions.

   Features:
   - Handles user input from a form or Enter key press.
   - Sends user input to a chatbot API for responses.
   - Stores the chat conversation in local storage.
   - Displays the chat history, including user inputs and chatbot responses.
   - Handles token count and message management.

   Author: Wes modes
   Date: 2023
*/

// Configurable variables
const tokenMax = 4000;
const tokenPaddingFactor = 0.2;
const tokenEstTHumbRuleFactor = 2.5

//Global variable to store the ongoing chat
var chat = [];
// Global variable to store the total number of chat tokens
let totalChatTokenCount = 0;
// const systemTokenCount = estimateTokenCount(systemContent);
const systemCharacterCount = systemContent.replace(/\s/g, '').length;
// global variable to store the client id
clientId = "";
const starters = [
  "Hey, how's it going?",
  "Hey, how can I help?",
  "You probably have limited time, so what can I do to help?",
  "Hey, thanks for coming. Whacha need?",
  "What's on your mind?",
  "Hey there, what's on your mind?",
  "Howdy! What can I help you with today?",
  "Yo, 'sup?",
  "Well, hello! What's the word?",
  "Hey, how can I help you today? Let me know if you have any questions or if there's anything specific you'd like to chat about.",
  "Yo, what's the story?",
  "I made it. What's up?",
]

// Render Details
//
// Marked
//
const mdRenderer = new marked.Renderer();
// Define a function to handle code blocks
// mdRenderer.code = (code, language) => {
//   // Return the code block as-is without any modification
//   return code;
// };
marked.use({
  renderer: mdRenderer,
});
// use with: const htmlContent = marked.parse(markdownText, mdOptions);
//
// shiki
//
syntaxTheme = 'nord';
// use with:
//     shiki.getHighlighter({
//       theme: 'nord',
//       langs: ['js'],
//     })
//     .then(highlighter => {
//       const code = highlighter.codeToHtml(`console.log('shiki');`, { lang: 'js' })
//       document.getElementById('output').innerHTML = code
//     })


//
// LOCAL STORAGE
//

// Get the client id from local storage (if it exists -- if not, generate one)
if (localStorage.getItem("clientId")) {
  clientId = localStorage.getItem("clientId");
} else {
  clientId = (Math.random() + 1).toString(36).substring(2, 14);
  localStorage.setItem("clientId", clientId);
}

// Check if the browser supports local storage
if (typeof(Storage) !== "undefined") {
  // Retrieve the chat from local storage
  chat = getChat();
  // estimate the token count of the chat
  totalChatTokenCount = estimateTokenCount(chat);
  
  if (chat.length === 0) {
    // If the stored chat is empty, initiate the chat
    $(document).ready(function() {
      initiateChat("");
    });
  } else {
    // If the stored chat is not empty, display the chat
    displayEntireChat();
  }
} else {
  // Browser does not support local storage, initiate chat normally
  $(document).ready(function() {
    initiateChat("");
  });
}

// Function to store the chat in local storage
function storeChat() {
  // Calculate the size of the chat in bytes (an estimate)
  var chatSize = JSON.stringify(chat).length;

  // Check if the chat size exceeds the 5MB limit
  if (chatSize + systemCharacterCount > 5 * 1024 * 1024) {

    // Determine how many elements to remove from the front of the array
    var elementsToRemove = 0;
    while (chatSize + systemCharacterCount > 5 * 1024 * 1024) {
      chatSize -= JSON.stringify(chat[elementsToRemove]).length;
      elementsToRemove++;
    }

    // Remove elements from the front of the array
    chat.splice(0, elementsToRemove);
  }

  // Store the chat array in local storage
  localStorage.setItem("chat", JSON.stringify(chat));
}


// Function to retrieve the chat from local storage
function getChat() {
  // Retrieve the chat array from local storage
  var storedChat = localStorage.getItem("chat");
  
  if (storedChat) {
    chat = JSON.parse(storedChat);
  }

  return chat;
}

//
// USER INPUT
//

// Handle submission when the "Submit" button is clicked
$("#submit-button").on("click", function(e) {
  e.preventDefault(); // Prevent the form from submitting
  handleUserInput();
});

// Handle submission when the "Enter" key is pressed
$("#user-input").on("keypress", function(e) {
  if (e.which === 13 && !e.shiftKey) { // Check if Enter is pressed without Shift
    e.preventDefault();
    handleUserInput();
  }
});

//
// HANDLE INPUT AND RESPONSE
//

function initiateChat(userInput) {
  // sigh, we used to have a nice model generaated welcome msg here, 
  //    now we just have a random canned starter
  // sendRequest(userInput);
  // select random starter
  const starter = starters[Math.floor(Math.random() * starters.length)];
  // add the reply to the chat
  chat.push({ role: "assistant", content: starter });
  // Store the chat
  storeChat(); 
  // display the starter
  displayResponse(starter);
}

function handleUserInput() {
  var userInput = $("#user-input").val();
  if (userInput) {
    displayUserInput(userInput)
    addUserMsgToChat(userInput);
    sendRequest(userInput);
    $("#user-input").val(''); // Clear the input field
  }
}

function sendRequest(userInput) {
  // display entire chat to console:
  // console.log("Full chat:", chat);

  // Create an object with the chat
  var requestData = {
    messages: chat,
    client_id: clientId,
  };

  // Use $.ajax to make a POST request to the /api/chatbot endpoint
  $.ajax({
    type: "POST",
    url: "/api/chatbot",
    contentType: "application/json", // Set the content type to JSON
    data: JSON.stringify(requestData),
    success: function(response) {
      handleResults(response);
    },
    error: function(xhr, status, error) {
      // Log detailed error information to the console
      console.error("Ajax request failed - " + status + ": " + error);
      
      // Provide a generic error message to handleResults
      handleResults({
        reply: "I'm sorry, I had an error generating a response. Please try again later",
        tokens: -1,
        status: "error",
      });
    }
  });
}

function handleResults(response) {
  response_status = response['status'];
  if (response_status === "error") {
    // check if the response is an error
    // if so, display the error message
    displayResponse(response['reply']);
    return;
  }
  reply = response['reply'];
  tokens = response['tokens'];

  // extract the token count from the response object
  tokenCount = response['tokens'];
  // console.log("Token Count:", tokenCount);
  // record the token count
  totalChatTokenCount = tokenCount;

  // add the reply to the chat
  chat.push({ role: "assistant", content: reply });

  // Store the chat
  storeChat(); 
  // Display the results
  displayResponse(reply); 
}

//
// DISPLAY CHAT
//

function displayEntireChat() {
  for (var i = 0; i < chat.length; i++)  {
    if (chat[i].role === "user") {
      // check if user input exists
      if (chat[i].hasOwnProperty('content')) {
        displayUserInput(chat[i].content, false);
      }
    } else if (chat[i].role === "assistant") {
      if (chat[i].hasOwnProperty('content')) {
        displayResponse(chat[i].content, false);
      } 
    }
  }
}

function hitBottom(slowScroll = true) {
  if (slowScroll) {
    // Scroll to the bottom with a smooth animation
    $("#chat-wrapper").animate({ scrollTop: $("#chat-wrapper")[0].scrollHeight }, 500);
  } else {
    // Scroll to the bottom without animation
    $("#chat-wrapper").scrollTop($("#chat-wrapper")[0].scrollHeight);
  }
}

// Function to display user input
function displayUserInput(userInput, slowScroll = true) {
  // Render output for safety and appearance
  userInput = renderBetterOutput(userInput);
  // Implement the logic to display the user input
  $("#chat").append(`<div class="user-input"><div class="user-icon"><img src="/img/user-icon.png"></div><div class="text-wrapper">${userInput}</div></div>`);
  hitBottom(slowScroll);
}

function displayResponse(response, slowScroll = true) {
  // Render output for safety and appearance
  response = renderBetterOutput(response);
  // Implement the logic to display the chat results
  // Example: Append the chatbot response using string interpolation
  $("#chat").append(`<div class="chat-response"><div class="wes-icon"><img src="/img/wes-icon.png"></div><div class="text-wrapper">${response}</div></div>`);
  hitBottom(slowScroll);
}

// Attach a click event listener to the "New Chat" button
$(".new-chat-button").on("click", function() {
  clearChat(); // Clear the existing chat
  storeChat(); // Store an empty chat in storage
  initiateChat(""); // Initiate a new chat
});

// Function to clear the chat displayed on the page
function clearChat() {
  chat = []; // Clear the conversation variable in memory
  $("#chat").empty(); // Remove all chat elements
}

//
// RENDER OUTPUT
//

// Render output for safety and appearance
function renderOutput(text) {
  // Remove [[topic]] from the text
  text = text.replace(/\[\[([^\]]*)\]\](\n*)/g, '');

  // Render html inert
  text = text.replace(/</g, '&lt;');
  text = text.replace(/>/g, '&gt;');

  // Replace triple backticks with code blocks
  text = text.replace(/```([\s\S]*?)\n([\s\S]*?)```/g, '<div class="code-block"><div class="code-type">$1</div><div class="content">$2</div></div>');
   
  // Replace pairs of backticks with <tt> and </tt>
  text = text.replace(/`([\s\S]*?)`/g, '<b><tt>$1</tt></b>');

  // Replace pairs of asterisks on the same line with <i> and </i>
  text = text.replace(/\*([\s\S]*?)\*/g, '<i>$1</i>');

  // Replace pairs of double asterisks with <b> and </b>
  text = text.replace(/\*\*([\s\S]*?)\*\*/g, '<b>$1</b>');

  text = text.replace(/\n/g, '<br>');
  return text;
}

// Modify the renderHTMLInert function to escape angle brackets outside of code blocks
// This will take input text:
//       ```html
//       <div>Hello</div>
//       ```
//       <div> is a division within the HTML. `<\div>` is a closing tag.
// And should return:
//       ```html
//       <div>Hello</div>
//       ```
//       &lt;div&gt; is a division within the HTML. `<\div>` is a closing tag.
//
function renderHTMLInert(text) {
  // Use regular expressions to identify and escape angle brackets outside of code blocks
  text = text.replace(/```(?:[\s\S]*?)```|<pre><code[^>]*>[\s\S]*?<\/code><\/pre>|`[^`]*`|<(?!\/?code\b)[^<]+>/g, function (match) {
    if (/```/.test(match) || /`[^`]*`/.test(match)) {
      // Preserve code blocks and content within backticks
      return match;
    } else {
      // Escape angle brackets outside of code blocks
      return match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }
  });
  return text;
}



function getPrismCodeType(codeType) {
  // Check if the codeType exists in the formatTable
  const formatTable = {
    "javascript": "js",
    // "python": "py",
    "c++": "cpp",
    "c#": "csharp",
    "shell:": "shellsession",
      
    "markdown": "md",
    "ruby": "rb",
    "plain text": "plaintext",
  }
  var newCodeType;
  if (formatTable[codeType]) {
    newCodeType = formatTable[codeType];
  } else {
    // If not found, return the original codeType
    newCodeType = codeType;
  }
  return newCodeType;
}

// Render output for safety and appearance
// This will take input text:
//    ```python
//    print("hello world")
//    ```
function renderBetterOutput(text) {

  // Step 1: Sanitize inputText to make all HTML inert
  text = renderHTMLInert(text);

  // Step 2: Process the sanitizedText using Marked.js to convert Markdown to HTML
  text = marked.parse(text);

  // Step 3: Find code blocks, i.e., <pre><code>...</code></pre> and wrap with our custom code
  // Wrap the text in a jQuery object
  const $text = $('<div>').html(text);
  $text.find('pre code').each(function () {
    const codeType = $(this).attr('class').replace('language-',''); // Extract code type
    const codeContent = $(this).html(); // Extract code content

    const prismCodeType = getPrismCodeType(codeType);

    // Create a custom code block
    const customCodeBlock = `
      <div class="code-block">
        <div class="code-type">${codeType}</div>
        <div class="content">
          <pre><code class="language-${prismCodeType}">${codeContent}</code></pre>
        </div>
      </div>`;

    // Convert the customCodeBlock into an element
    const $customCodeBlock = $(customCodeBlock);

    // Run Prism's highlightElement on the custom code block
    Prism.highlightElement($customCodeBlock.find('code')[0]);

    // Replace the original code block with the custom code block
    $(this).closest('pre').replaceWith($customCodeBlock);
  });

  // Step 4: Return the HTML content for rendering on the webpage
  return $text.html();
}




//
// TOKENIZATION
//

// Function to estimate token count
// function estimateTokenCount(data) {
//   // Flatten the data structure into a single string using JSON.stringify
//   const flattenedText = JSON.stringify(data);

//   // Estimate tokens in the flattened text
//   return flattenedText.split(/\s+/).length;
// }

// A helpful rule of thumb is that one token generally corresponds to ~4 characters of text 
// for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words).
function estimateTokenCount(data) {

  if (! data) {
    return 0;
  }
  // Flatten the data structure into a single string using JSON.stringify
  const flattenedText = JSON.stringify(data);

  // Estimate tokens based on character count divided by tokenEstTHumbRuleFactor
  const estimatedTokens = Math.ceil(flattenedText.length / tokenEstTHumbRuleFactor);

  return estimatedTokens;
}


// Function to add a new message to the conversation and update token count
function addUserMsgToChat(userInput) {
  const newMessage = { role: "user", content: userInput };
  // add new message to chat
  chat.push(newMessage);

  // estimate new message token count
  const estMsgTokenCount =  estimateTokenCount(newMessage);

  // temporary variable to store the est token count
  let estTotalTokenCount = totalChatTokenCount + estMsgTokenCount ;

  // Check if the total token count exceeds the model's maximum context length
  // minus a padding factor padded to leave 20% extra capacity
  if (estTotalTokenCount > tokenMax * (1 - tokenPaddingFactor)) {
    // Remove the oldest message(s) from the chat to bring it under the token limit
    while (estTotalTokenCount > tokenMax * (1 - tokenPaddingFactor)) {
      const oldestMessage = chat.shift();
      // con  sole.log("Trimming oldest message:", oldestMessage)
      const estOldMsgTokenCount = estimateTokenCount(oldestMessage);
      estTotalTokenCount -= estOldMsgTokenCount;
    }
  }

  // console.log("Reported total token count:", totalChatTokenCount);  
  // console.log("Est new total token count:", estTotalTokenCount);
}