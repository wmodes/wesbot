
//Global variable to store the ongoing chat
var chat = [];

// Initialize a variable to keep track of the token count
let tokenCount = 0;
const systemTokenCount = 702;
const systemCharacterCount = 4523;

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
    addMessageToChat(userInput);
    sendRequest(userInput);
    $("#user-input").val(''); // Clear the input field
  }
}

function sendRequest(userInput) {
  // display entire chat to console:
  console.log("Full chat:", chat);

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
    success: function(data) {
      handleResults(data.response);
    },
    error: function(xhr, status, error) {
      // Log detailed error information to the console
      console.error("Ajax request failed - " + status + ": " + error);
      
      // Provide a generic error message to handleResults
      handleResults("Chatbot: An error occurred. Please try again later.");
    }
  });
}

function handleResults(response, userInput) {
  chat.push({ role: "assistant", content: response });

  storeChat(); // Store the chat
  displayResponse(response); // Display the results
}

//
// LOCAL STORAGE
//

// Check if the browser supports local storage
if (typeof(Storage) !== "undefined") {
  // Retrieve the chat from local storage
  chat = getChat();
  
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
      displayUserInput(chat[i].content);
    } else if (chat[i].role === "assistant") {
      displayResponse(chat[i].content);
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

// Function to calculate token count
function calculateTokenCount(message) {
  // This is a simplified way to count tokens and may not be as accurate as OpenAI's official libraries
  return message.content.split(/\s+/).length;
}

// Function to add a new message to the conversation and update token count
function addMessageToChat(userInput) {
  const newMessage = { role: "user", content: userInput };
  //TODO: Implement the logic to add a new message to the conversation and update token count
  const newMessageTokens = calculateTokenCount(newMessage);

  // Check if adding the new message will exceed the token limit
  while (tokenCount + newMessageTokens > 4096) {
    // Remove the oldest message from the chat
    const oldestMessage = chat.shift();
    const oldestMessageTokens = calculateTokenCount(oldestMessage);

    // Update the token count
    tokenCount -= oldestMessageTokens;
  }

  chat.push(newMessage);
  tokenCount += newMessageTokens;
  console.log("Token count:", tokenCount);
}