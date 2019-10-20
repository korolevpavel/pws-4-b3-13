class Tag:
    # ...


class HTML:
    # ...


class TopLevelTag:
     def __init__(self, tag):
        self.tag = tag
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def __str__(self):
        html = "<%s>\n" % self.tag
        for child in self.children:
            html += str(child)
        html += "\n</%s>" % self.tag
        return html


def main(output=None):
    with HTML(output=None) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png") as img:
                    div += img

                body += div

            doc += body


if __name__ == "__main__":
    main("index.html")
