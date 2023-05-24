# SWAPI Explorer

The SWAPI Explorer is a simple command-line Python application that allows users to explore data from the Star Wars API (SWAPI). Users can retrieve and view data about Star Wars films and characters.

## Requirements

- Python 3.6+
- requests

## Installation

First, clone this repository:

```bash
git clone https://github.com/yourusername/swapi-explorer.git
cd swapi-explorer
```

Next, install the requests library:

```bash
pip install requests
```

## Usage

To start the application, run the following command in your terminal:

```bash
python main.py
```

The application will present you with a menu:

```
1. Get information about a film
2. Get information about a person
3. Quit
Choose an option:
```

You can enter the number corresponding to the option you want.

If you choose options 1 or 2, you will be asked to enter the ID of a film or person, respectively. The application will then fetch the data from SWAPI and print it to the console.

To quit the application, choose option 3.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Please replace "yourusername" with your actual GitHub username in the git clone URL. The rest of the README can be used as is. Also, you can include the `LICENSE` file in your repository if you want to license your project under the MIT License.
