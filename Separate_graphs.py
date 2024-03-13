import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data setup
categories_efficiency = ['Time Reduction', 'Coding Efficiency']
significant_improvement = [57, 57]  # Significant improvement percentages
somewhat_improvement = [43, 43]  # Somewhat improvement percentages

# Quality of work data for pie chart
quality_labels = ['Significant Improvement', 'Somewhat Improvement']
code_quality = [71, 29]  # percentages

# Learning and Development data for horizontal bar
learning_development = [29, 71]  # Great and moderate improvements

# DevBot Users Distribution data for pie chart
user_types = ['UI Dev', 'Backend Dev', 'AWS Dev', 'Junior AI Dev']
num_people = [5, 5, 4, 3]  # Distribution of the 17 people

# Create subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Efficiency Improvements', 'Code Quality', 'Learning and Development', 'DevBot Users Distribution'),
    specs=[[{"type": "bar"}, {"type": "pie"}], [{"type": "bar"}, {"type": "pie"}]]
)

# Efficiency Improvements - Bar Chart
fig.add_trace(
    go.Bar(name='Significant Improvement', x=categories_efficiency, y=significant_improvement, marker_color='green'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(name='Somewhat Improvement', x=categories_efficiency, y=somewhat_improvement, marker_color='darkblue'),
    row=1, col=1
)

# Code Quality - Pie Chart
fig.add_trace(
    go.Pie(labels=quality_labels, values=code_quality, marker_colors=['green', 'lightblue']),
    row=1, col=2
)

# Learning and Development - Horizontal Bar Chart
fig.add_trace(
    go.Bar(name='Learning and Development', x=learning_development, y=['Great', 'Moderate'], marker_color=['green', 'lightgreen'], orientation='h'),
    row=2, col=1
)

# DevBot Users Distribution - Pie Chart
fig.add_trace(
    go.Pie(labels=user_types, values=num_people, marker_colors=['skyblue', 'mediumseagreen', 'salmon', 'violet']),
    row=2, col=2
)

# Update layout for clarity and readability
fig.update_layout(
    title='Comprehensive Impact Analysis of Developer Assistant Bot',
    height=1200,  # Adjusted for better visibility in the write-up
    width=1000
)

# Show the figure
fig.show()
