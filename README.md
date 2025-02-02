## Django Tailwind Project

`cd static`

`npm init -y`

`npm install -D tailwindcss@3 postcss autoprefixer`

`npx tailwindcss init` This Command will create `tailwind.config.js` and then Change content like this to find django templates:

```
content: [
    '../templates/**/*.html',
],
```

add `"go": "npx tailwindcss -i ./src/input.css -o ./src/output.css"` to `package.json` > `scripts`

then run `npm run go`