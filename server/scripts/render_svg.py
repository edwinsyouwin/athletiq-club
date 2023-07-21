import streamlit as st
import base64
import textwrap

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def render_svg_example():
    svg = """
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """
    st.write('## Rendering an SVG in Streamlit')

    st.write('### SVG Input')
    st.code(textwrap.dedent(svg), 'svg')

    st.write('### SVG Output')
    render_svg(svg)

if __name__ == '__main__':
    render_svg_example()