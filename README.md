# Automated Toll Tax System
Automated Toll Tax System using Number Plate Recognition is a comprehensive solution designed to simplify and streamline toll tax collection processes. This system utilizes advanced number plate recognition technology to accurately detect and recognize vehicle number plates. It marks the entry of vehicles and records transactions for registered entries, ensuring a seamless toll tax collection experience.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the command: `pip install -r requirements.txt`.
3. Open the `connection.py` file and modify the database connection settings to match your environment.
4. Update the values of the database host, port, username, password, and database name to reflect your own database configuration.
5. Save the changes in the `connection.py` file.
6. Run the application using the command: `python mainFile.py`.

## Usage

1. Ensure that the system is up and running.
2. Choose one of the following options:
   - Click on the "Camera" button to capture an image using the connected camera for number plate recognition.
   - Click on the "Select Image" button to choose an image file from your computer for number plate recognition.
3. The system will process the selected image, detect the number plate, and mark the entry of the vehicle.
4. For registered vehicles, the system calculates and records the toll tax transaction.
5. Access the generated transaction records in the database or through the provided user interface for monitoring and management.

## Configuration

- Modify the database connection settings in the `connection.py` file to match your environment.
- Update the values of the database host, port, username, password, and database name in the `connection.py` file.
- Save the changes in the `connection.py` file.

## Dependencies

- This project utilizes the `tkinter` library for creating the user interface. Ensure that it is installed by running the command: `pip install tkinter`.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements.

## Roadmap

- Improve the accuracy of number plate recognition.
- Enhance the user interface for better system management and reporting.
- Implement additional features such as real-time alerts and statistical analysis.

