
# Fluent Android Chatbot

## Overview

This project focuses on building a custom Android chatbot integrated with Microsoft's Fluent Design System. The chatbot is designed to answer queries related to Fluent, leveraging AI-based prompt engineering techniques. Additionally, the repository includes a **Dataset Creator Tool** that fetches data from a GitHub repository and creates a JSON file, which can be used as a training dataset for the chatbot.

## Table of Contents
- [Introduction to Fluent Design](#introduction-to-fluent-design)
- [Chatbot Functionality](#chatbot-functionality)
- [Dataset Creator Tool](#dataset-creator-tool)
  - [How the Training Dataset is Created](#how-the-training-dataset-is-created)
  - [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction to Fluent Design

Fluent Design is Microsoft's design system aimed at creating intuitive, engaging, and beautiful user experiences across devices and platforms. The system is built around five key principles:

1. **Light**: Creates depth and guides users' attention with shadowing and lighting techniques.
2. **Depth**: Enhances the 3D feel of the UI by introducing layers and shadow effects.
3. **Motion**: Adds fluidity and interactivity to the UI, ensuring smooth transitions between states.
4. **Material**: Provides a natural and tactile experience through intuitive interactions.
5. **Scale**: Ensures consistent design across multiple platforms and devices.

The FluentUI library provides components and styles based on these principles, and the Fluent Android Chatbot follows these guidelines to create a visually consistent user experience.

## Chatbot Functionality

The Fluent Android Chatbot is a custom-built bot that helps users understand and interact with Microsoft's Fluent Design. Here’s how it works:

1. **User Queries**: Users can ask the chatbot questions related to Fluent Design, such as "What are Fluent Design principles?" or "How do I implement depth in my Android app?"
   
2. **Natural Language Processing**: The chatbot uses custom AI prompts designed with **Microsoft Copilot Studio**. It processes these queries and provides accurate and contextually relevant responses.

3. **Response Generation**: Based on the training data and the prompt design, the bot responds with detailed answers. It is capable of handling both basic and complex questions about Fluent design, UI elements, and design patterns.

4. **Continuous Learning**: The chatbot’s knowledge can be expanded by training it with additional data using the Dataset Creator Tool, allowing for continuous improvements.

## Dataset Creator Tool

The **Dataset Creator Tool** is a Python-based utility that automates the process of creating a training dataset for the chatbot. It pulls data from a GitHub repository and generates a JSON file that can be used to train the bot.

### How the Training Dataset is Created

1. **Data Fetching**: The tool is configured to fetch relevant data from a specified GitHub repository. The data includes structured question-answer pairs related to Fluent Design concepts.

2. **Data Processing**: The fetched data is processed and structured into JSON format. The tool organizes the data into a format that can be used to train the chatbot’s machine learning model.

3. **Output**: The final JSON file contains a collection of questions and corresponding answers, which serve as the training dataset for the chatbot.

The Python tool ensures that the dataset remains up-to-date by pulling the latest information from the GitHub repository, allowing the bot to provide more accurate and comprehensive answers.

### Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ayanshakil/Fluent-Android-Chatbot.git
   cd Fluent-Android-Chatbot
2. **Navigate to the Dataset Creator Tool**:
   ```bash
   cd dataset-creator-tool
3. **Run the Python Tool**:
   ```bash
   python dataset_creator.py
This will fetch data from the GitHub repository and generate a JSON file containing the training data.
4. **Use the Generated JSON**: 
The output JSON file can be used to train the chatbot, ensuring that it is equipped with up-to-date information about Fluent Design.

## Tech Stack
1. **Android (Java/Kotlin)**: For developing the core chatbot application.
2. **FluentUI Library**: To implement Fluent's design principles.
3. **Python**: For creating the Dataset Creator Tool.
4. **GitHub**: As the data source for training datasets.
5. **Microsoft Copilot Studio**: For crafting chatbot prompts and response mechanisms.

## ScreenShots: 
![Screenshot 2024-10-15 050225](https://github.com/user-attachments/assets/0bd49747-a88e-4c1c-9605-69be8feeaa93)
![Screenshot 2024-10-15 045927](https://github.com/user-attachments/assets/fec9b69b-187b-4ddb-8f09-9d611b85c67e)
![Screenshot 2024-10-15 050213](https://github.com/user-attachments/assets/fbf2b45c-7744-44b4-8c14-4d33a1b64141)
![Screenshot 2024-10-15 050156](https://github.com/user-attachments/assets/239d4c48-6497-4b15-88a7-14f580ee7fea)



## Contributing
We welcome contributions! If you would like to contribute, please fork the repository and create a pull request. Make sure your changes align with the project goals.

## License
This project is licensed under the MIT License - see the LICENSE file for details.





