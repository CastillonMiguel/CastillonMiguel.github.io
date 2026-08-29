Visual Studio Code 🔵 
=====================

🚀 **Introduction** 🚀
-----------------------
**Visual Studio Code (VS Code)** is a lightweight yet powerful code editor developed by Microsoft. It is widely used across multiple domains, including scientific research and software development, due to its versatility, customization options, and rich ecosystem of extensions. Whether you're coding in Python, C++, or any other language, VS Code provides an intuitive and efficient development environment.


🔍 **Why Use VS Code for Research?** 🔍
--------------------------------------
VS Code is highly regarded in the research community for the following reasons:

- **🖥️ Cross-platform**: Available on Windows, macOS, and Linux, making it accessible to everyone.
- **⚡ Lightweight**: Unlike full-fledged IDEs, it is fast to load and easy on system resources, yet still powerful.
- **🔌 Extensibility**: With thousands of extensions, you can customize VS Code to support nearly any programming language, debugging tools, version control (Git), and specialized features for research.
- **📟 Integrated Terminal**: You can run your scripts, compile code, or manage your version control without leaving the editor.
- **📊 Jupyter Notebooks Support**: Native support for Jupyter Notebooks, particularly useful for researchers working with Python, machine learning, and data analysis.

🎯 **Key Features** 🎯
----------------------
1. **💻 Integrated Development Environment (IDE) Features**
   - IntelliSense provides code completions, parameter hints, and documentation support for various programming languages.
   - Built-in debugging tools help identify and resolve issues in your code effectively.

2. **🛠️ Extensions Marketplace**
   - Install extensions like Python, C++, LaTeX Workshop, and more to adapt the editor to your research needs.
   - Popular extensions for computational mechanics, numerical computing, and web development are available.

3. **🔗 Version Control with Git**
   - Seamlessly integrates with Git for version control, making it easy to manage your research code, track changes, and collaborate with others.

4. **🌍 Remote Development**
   - VS Code supports remote development, allowing you to connect to servers or containers and edit code as if it were local—great for working on research clusters or cloud systems.

🚀 **Getting Started** 🚀
-------------------------
1. The first step is to download and install `Visual Studio Code <https://code.visualstudio.com>`__.
2. Install extensions based on your needs (e.g., Python, C++, or Jupyter Notebooks).
3. Configure your workspace with settings tailored to your research workflow.
4. Start coding, debugging, and managing projects all in one place!

In short, **VS Code** is an excellent tool for researchers due to its flexibility, speed, and the broad range of features it offers to streamline your development process.

🔌 **Extensions** 🔌
---------------------
Below are some useful extensions that I have used:

**C++ Programming Extensions** 🔧
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Name**: C/C++  
  **Description**: C/C++ IntelliSense, debugging, and code browsing.

- **Name**: C/C++ Extension Pack  
  **Description**: Popular extensions for C++ development in Visual Studio Code.

- **Name**: C/C++ Themes  
  **Description**: UI Themes for C/C++ extension.

**Python Programming Extensions** 🐍
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These extensions are helpful for Python development:

- **Name**: autopep8  
  **Description**: Automatically formats Python code to conform to the PEP 8 style guide.

- **Name**: Python  
  **Description**: Official Python extension for Visual Studio Code. Provides Python language support, including IntelliSense, linting, and debugging.

- **Name**: Pylance  
  **Description**: Fast and feature-rich Python language server, providing type checking and IntelliSense for Python.

- **Name**: Python Environment Manager  
  **Description**: Manage multiple Python environments within Visual Studio Code.

**Other Useful Extensions** 🌟
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These extensions enhance general development and productivity in Visual Studio Code:

- **Name**: Git Graph  
  **Description**: Visualize and interact with your Git repository.

- **Name**: Remote - SSH  
  **Description**: Develop on remote machines using SSH.

- **Name**: Remote Explorer  
  **Description**: Explore and manage remote workspaces.

- **Name**: VS Code Icons  
  **Description**: A set of icons to visually enhance file types in the explorer.

**Documentation Extensions** 📝
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These extensions are useful for writing and previewing documentation:

- **Name**: reStructuredText Syntax Highlighting  
  **Description**: Adds syntax highlighting for `.rst` files.

- **Name**: RST Preview  
  **Description**: Preview reStructuredText documents as HTML in Visual Studio Code.

- **Name**: Gmsh Language for VS Code  
  **Description**: Provides language support for Gmsh, a finite element mesh generator.

🗂️ **launch.json, settings.json, and tasks.json** 🗂️
-----------------------------------------------------
launch.json, settings.json, and tasks.json are configuration files commonly used in the development of applications and software projects.

**launch.json** 🚀
^^^^^^^^^^^^^^^^^^
Defines how a debugger should launch and attach to a specific program or application.

**settings.json** ⚙️
^^^^^^^^^^^^^^^^^^^
Stores various settings and preferences for a development environment or IDE.

**tasks.json** 📋
^^^^^^^^^^^^^^^^^
Defines and configures tasks or build processes within an IDE or development environment.

Files:
------

The files that organize the JSON project are in a hidden folder named `.vscode`.

.. note::
   To view hidden files on a Mac, use the keyboard command **Command + Shift + .**

.. code-block:: console

   project/
     ├── .vscode
               ├── launch.json
               ├── settings.json
               └── tasks.json