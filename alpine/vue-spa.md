# Santa Good/Naught list in Vue.js

Disclaimer: I'll be using the Options API.
This whole tutorial is a Christmas remix on [MDN Vue tutorial](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started) and the [official Vue.js tutorial](https://vuejs.org/tutorial).

## Tasks

1. Create a boilerplate project with `npm create vue@latest`. Install the necessary scripts with `npm install` inside the project and run the debug server `npm run dev`. You can also try the [Vue playground](https://play.vuejs.org/)!
3. Use a chosen classless CSS, we don't have time for looks today.
4. Create a component that will display a single person. Use data fields and templating forthis.
5. Show their good and bad deeds as other components. Use list rendering and props for this.
6. Color the name of the fool based on their balance. Use `v-bind:class` for this. Try also adding a label using conditional rendering.
7. Use `v-model`, `v-on` to add a way to create new records, render them using list rendering.
8. The Santa should be able to add new deeds and edit old deeds. No reason to let him remove anything though. You can't change the past. Try creating a custom input popups for this using event listening, and emitting.
9.  Check if the labels and coloring still work properly and use Watchers if they do not.
10. Add a JSON export.

## Some info from the Vue boilerplate

### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

### Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

### Project Setup

```sh
npm install
```

#### Compile and Hot-Reload for Development

```sh
npm run dev
```

#### Compile and Minify for Production

```sh
npm run build
```
