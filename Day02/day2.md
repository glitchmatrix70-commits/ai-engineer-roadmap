# Day 2 – APIs & JSON | Interview Questions & Answers

---

## Question 1

### What is an API?

**Interview Answer (1–2 lines):**  
An API (Application Programming Interface) is a set of rules that allows two software applications to communicate and exchange data with each other.

**Real-life Example:**  
Like a waiter in a restaurant—the waiter takes your order to the kitchen and brings back your food without you interacting with the chef directly.

---

## Question 2

### Difference between Website and API

| Website | API |
|----------|-----|
| Built for humans to view and interact with. | Built for software applications to exchange data. |
| Returns HTML, CSS, images, etc. | Usually returns JSON or XML data. |
| Opened in a web browser. | Accessed using code or HTTP requests. |

**Real-life Example:**  
A website is like the menu you read in a restaurant, while an API is like the waiter who communicates your order to the kitchen.

---

## Question 3

### Difference between GET and POST

| GET | POST |
|-----|------|
| Used to retrieve data from a server. | Used to send data to a server. |
| Data is sent in the URL. | Data is sent in the request body. |
| Doesn't modify server data. | Usually creates or updates data. |

**Real-life Example:**  
**GET** is like asking a librarian for a book.  
**POST** is like submitting a new book to the library.

---

## Question 4

### What is JSON?

**Interview Answer (1–2 lines):**  
JSON (JavaScript Object Notation) is a lightweight text format used to store and exchange data between applications. It is easy for both humans and machines to read.

**Real-life Example:**  
Like a digital form where every field has a label and a value, such as `"name": "John"` and `"age": 25`.

---

## Question 5

### Why do AI Engineers use APIs every day?

**Interview Answer (1–2 lines):**  
AI engineers use APIs to connect their applications with AI models, databases, cloud services, payment systems, and third-party tools without building everything from scratch.

**Real-life Example:**  
Instead of building your own weather station, you use a weather API to get the latest weather data instantly.

---

## Question 6

### How does ChatGPT answer your question?

1. You type a prompt.
2. Your application sends an HTTP request to the OpenAI server.
3. The server receives the request and forwards it to the language model.
4. The LLM processes your prompt and generates a response.
5. The response is returned as JSON.
6. Your application reads the JSON and displays the answer.

**Real-life Example:**  
Like sending a question to customer support—they receive your request, prepare an answer, and send it back for you to read.

---

## Question 7

### Why do we use `response.json()` instead of `response.text`?

**Interview Answer (1–2 lines):**  
We use `response.json()` because it converts JSON data into Python dictionaries and lists, making it easy to access individual values. `response.text` only returns the raw text.

**Real-life Example:**  
`response.text` is like receiving an unopened package, while `response.json()` is like opening the package and organizing its contents so you can use them immediately.

**Example:**

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.text)      # Raw JSON string
print(response.json())    # Python dictionary
```

After using `response.json()`:

```python
data = response.json()

print(data["name"])
print(data["email"])
```

This is much easier than manually parsing a text string.

---

# Quick Revision

- **API** → Allows two applications to communicate.
- **Website** → Built for humans.
- **API** → Built for software.
- **GET** → Retrieve data.
- **POST** → Send or create data.
- **JSON** → Standard format for exchanging data.
- **AI Engineers** → Use APIs to access AI models and external services.
- **ChatGPT Workflow** → Prompt → HTTP Request → Server → LLM → JSON Response → Display.
- **`response.json()`** → Converts JSON into Python objects.
- **`response.text`** → Returns raw text only.