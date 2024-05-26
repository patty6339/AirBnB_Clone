This is the file for web static project

### What is HTML

HTML (HyperText Markup Language) is the standard language used to create and design the structure of web pages. It uses a series of elements or tags to denote different parts of a web page, such as headings, paragraphs, links, images, and other types of content. HTML provides the skeleton of a web page that can be styled with CSS and made interactive with JavaScript.

### How to Create an HTML Page

1. Open a text editor (e.g., Notepad, Sublime Text, VS Code).
2. Write the following basic HTML structure:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My First HTML Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is my first HTML page.</p>
    </body>
    </html>
    ```

3. Save the file with a `.html` extension, for example, `index.html`.
4. Open the saved HTML file in a web browser to view the web page.

### What is a Markup Language

A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. It uses tags or elements to define the structure and presentation of text. HTML is a type of markup language that is specifically designed for creating web pages.

### What is the DOM

The DOM (Document Object Model) is a programming interface for web documents. It represents the structure of a document as a tree of objects, with each object corresponding to a part of the document, such as an element, attribute, or text. The DOM allows programming languages like JavaScript to manipulate the content, structure, and style of a web page dynamically.

### What is an Element / Tag

An element (or tag) in HTML is a building block of a web page. An HTML element typically consists of an opening tag, content, and a closing tag. For example, `<p>This is a paragraph.</p>` is a paragraph element where `<p>` is the opening tag, `This is a paragraph.` is the content, and `</p>` is the closing tag.

### What is an Attribute

An attribute provides additional information about an HTML element. Attributes are specified within the opening tag and usually come in name/value pairs, for example:

```html
<a href="https://www.example.com">Visit Example</a>
```

In this example, `href="https://www.example.com"` is an attribute of the `<a>` (anchor) tag that specifies the URL to which the link should navigate.

### How Does the Browser Load a Webpage

1. **URL Request**: The browser requests the webpage by sending a URL to a web server.
2. **Response**: The server responds with the HTML content of the page.
3. **Parsing HTML**: The browser parses the HTML and builds the DOM.
4. **Fetching Resources**: The browser fetches additional resources such as CSS, JavaScript, and images referenced in the HTML.
5. **Building CSSOM**: The browser parses CSS and builds the CSS Object Model (CSSOM).
6. **Rendering**: The browser combines the DOM and CSSOM into a Render Tree.
7. **Layout**: The browser calculates the layout of each element.
8. **Painting**: The browser paints the pixels to the screen.

### What is CSS

CSS (Cascading Style Sheets) is a language used to describe the presentation of a web page written in HTML. CSS defines how HTML elements should be displayed, including their layout, colors, fonts, and other visual aspects.

### How to Add Style to an Element

1. **Inline Styles**: Directly within an HTML element using the `style` attribute.

    ```html
    <p style="color: blue; font-size: 20px;">This is a styled paragraph.</p>
    ```

2. **Internal Stylesheet**: Within a `<style>` tag in the `<head>` section of the HTML document.

    ```html
    <head>
        <style>
            p {
                color: blue;
                font-size: 20px;
            }
        </style>
    </head>
    ```

3. **External Stylesheet**: In a separate CSS file linked to the HTML document.

    ```html
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    ```

    ```css
    /* styles.css */
    p {
        color: blue;
        font-size: 20px;
    }
    ```

### What is a Class

A class is an attribute used in HTML to define a group of elements that can be styled in the same way with CSS. Classes are defined using the `class` attribute.

```html
<p class="highlight">This is a highlighted paragraph.</p>
```

```css
/* CSS */
.highlight {
    background-color: yellow;
    font-weight: bold;
}
```

### What is a Selector

A selector is a pattern used in CSS to select the elements you want to style. Selectors can be based on element names, classes, IDs, attributes, and more.

```css
/* Element selector */
p {
    color: blue;
}

/* Class selector */
.highlight {
    background-color: yellow;
}

/* ID selector */
#unique {
    font-size: 24px;
}
```

### How to Compute CSS Specificity Value

CSS specificity determines which styles are applied to an element when multiple rules could apply. Specificity is calculated based on the types of selectors used:

1. **Inline styles** (style attribute) have the highest specificity.
2. **ID selectors** (#id) are more specific than classes, attributes, and pseudo-classes.
3. **Class selectors** (.class), attributes selectors ([attribute]), and pseudo-classes (:hover) have lower specificity than ID selectors.
4. **Element selectors** (div, p) and pseudo-elements (::before) have the lowest specificity.

Specificity is calculated as a four-part value (a, b, c, d):

- a: Inline styles
- b: Number of ID selectors
- c: Number of class, attribute, and pseudo-class selectors
- d: Number of element and pseudo-element selectors

For example:

```html
<div id="unique" class="highlight example">
    <p>This is a paragraph.</p>
</div>
```

```css
/* Specificity: 0-1-1-1 (ID, class, element) */
#unique .highlight p {
    color: red;
}
```

### What are Box Properties in CSS

The CSS Box Model represents the rectangular boxes generated for elements in the document tree and consists of:

1. **Content**: The actual content of the element.
2. **Padding**: The space between the content and the border.
3. **Border**: The border surrounding the padding (and content).
4. **Margin**: The space outside the border, separating the element from other elements.

Box properties include:

- `width` and `height`: Size of the content area.
- `padding`: Space between the content and border.
- `border`: Defines the border's width, style, and color.
- `margin`: Space outside the border, creating distance from other elements.

Example:

```css
.box {
    width: 200px;
    height: 100px;
    padding: 10px;
    border: 2px solid black;
    margin: 20px;
}
```