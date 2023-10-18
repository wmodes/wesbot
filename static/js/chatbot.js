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
  sendRequest(userInput);
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
  if (response['status'] === "error") {
    // check if the response is an error
    // if so, display the error message
    displayResponse(response['reply']);
    return;
  }
  // console.log("handleResults Response:", response)
  // extract the assistant response from the response object
  reply = response['reply'];
  // console.log("Reply:", reply);
  // add the reply to the chat
  chat.push({ role: "assistant", content: reply });

  // extract the token count from the response object
  tokenCount = response['tokens'];
  // console.log("Token Count:", tokenCount);
  // record the token count
  totalChatTokenCount = tokenCount;

  // Store the chat
  storeChat(); 
  // Display the results
  displayResponse(reply); 
}

//
// LOCAL STORAGE
//

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
// DISPLAY CHAT
//

function displayEntireChat() {
  for (var i = 0; i < chat.length; i++)  {
    if (chat[i].role === "user") {
      // check if user input exists
      if (chat[i].hasOwnProperty('content')) {
        displayUserInput(chat[i].content);
      }
    } else if (chat[i].role === "assistant") {
      if (chat[i].hasOwnProperty('content')) {
        displayResponse(chat[i].content);
      } 
    }
  }
}

function displayUserInput(userInput) {
  userInput = renderOutput(userInput);

  $("#chat").append(`<div class="user-input">${userInput}</div>`);
  // Scroll to the bottom with a smooth animation
  $("#chat-wrapper").animate({ scrollTop: $("#chat-wrapper")[0].scrollHeight }, 500);
}

function displayResponse(response) {
  // Render output for safety and appearance
  response = renderOutput(response);
  // Implement the logic to display the chat results
  // Example: Append the chatbot response using string interpolation
  $("#chat").append(`<div class="chat-response">${response}</div>`);
  // Scroll to the bottom with a smooth animation
  $("#chat-wrapper").animate({ scrollTop: $("#chat-wrapper")[0].scrollHeight }, 500);
}

// Attach a click event listener to the "New Chat" button
$("#new-chat-button").on("click", function() {
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
  text = text.replace(/</g, '&lt;');
  text = text.replace(/>/g, '&gt;');
  // Replace triple backticks with code blocks
  text = text.replace(/```([\s\S]*?)\n([\s\S]*?)```/g, '<div class="code"><div class="code-type">$1</div><div class="content">$2</div></div>');
   
  // Replace pairs of backticks with <tt> and </tt>
  text = text.replace(/`([\s\S]*?)`/g, '<b><tt>$1</tt></b>');

  // Replace pairs of asterisks on the same line with <i> and </i>
  text = text.replace(/\*([\s\S]*?)\*/g, '<i>$1</i>');

  // Replace pairs of double asterisks with <b> and </b>
  text = text.replace(/\*\*([\s\S]*?)\*\*/g, '<b>$1</b>');

  text = text.replace(/\n/g, '<br>');
  return text;
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
  const estMsgTokenCount = estimateTokenCount(newMessage);

  // temporary variable to store the est token count
  let estTotalTokenCount = totalChatTokenCount + estMsgTokenCount ;

  // Check if the total token count exceeds the model's maximum context length
  // minus a padding factor padded to leave 20% extra capacity
  if (estTotalTokenCount > tokenMax * (1 - tokenPaddingFactor)) {
    // Remove the oldest message(s) from the chat to bring it under the token limit
    while (estTotalTokenCount > tokenMax * (1 - tokenPaddingFactor)) {
      const oldestMessage = chat.shift();
      // console.log("Trimming oldest message:", oldestMessage)
      const estOldMsgTokenCount = estimateTokenCount(oldestMessage);
      estTotalTokenCount -= estOldMsgTokenCount;
    }
  }

  // console.log("Reported total token count:", totalChatTokenCount);  
  // console.log("Est new total token count:", estTotalTokenCount);
}