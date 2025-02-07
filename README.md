# Django Tailwind Sample

A sample setup for integrating **Tailwind CSS** with **Django**.

<img src="https://github.com/Mohammadshekari/Django-Tailwind-Sample/blob/main/screenshots/img.png?raw=true" width="500">

## Run Project

Clone the repository:

```sh
git clone https://github.com/Mohammadshekari/Django-Tailwind-Sample.git
cd Django-Tailwind-Sample
```

Navigate to the `tailwind` directory:

```sh
cd tailwind
```

Install libraries of NodeJS:

```sh
npm i
```

To watch files and update styles in real-time, run:

```sh
npm run dev
```

---

### Setting Up Tailwind in Your Django Project

Create and Navigate to the `tailwind` directory:

```sh
mkdir tailwind
cd tailwind
```

Initialize a `package.json` file:

```sh
npm init -y
```

Install Tailwind CSS, PostCSS, and Autoprefixer:

```sh
npm install -D tailwindcss@3 postcss autoprefixer
```

Initialize Tailwind CSS configuration:

```sh
npx tailwindcss init
```

This command creates a `tailwind.config.js` file.

Update the `content` section to scan Django templates:

```js
content: [
    '../templates/**/*.html',
],
```

### Adding Build Scripts

Modify your `package.json` and add these scripts under `scripts`:

```json
"scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ../static/src/output.css --watch --minify",
    "build": "npx tailwindcss -i ./src/input.css -o ../static/src/output.css --minify"
}
```

### Running the Development Server

To watch files and update styles in real-time, run:

```sh
npm run dev
```

To build the final, optimized CSS file, run:

```sh
npm run build
```

---

## Contributing

Feel free to open issues or submit pull requests! Contributions are welcome.

## License

This project is licensed under the **MIT License**.

## Author

👤 **Mohammad Shekari**

- GitHub: [@Mohammadshekari](https://github.com/Mohammadshekari)

---

This structure improves readability and adds **GitHub-related sections** like contributing, author details, and
licensing. 🚀