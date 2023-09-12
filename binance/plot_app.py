from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def plot_graph():
    # Create your data for the graph
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Plot the graph
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Graph')

    # Save the graph to a file
    graph_filename = 'static/graph.png'
    plt.savefig(graph_filename)

    # Render the template with the graph
    return render_template('graph.html', graph_filename=graph_filename)


