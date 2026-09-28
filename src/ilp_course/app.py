import ast
import gradio as gr
from .models import solve_knapsack, solve_assignment, solve_production, solve_facility_location


def parse_vector(s):
    return ast.literal_eval(s)


def knapsack_ui(values, weights, capacity):
    try:
        v = parse_vector(values)
        w = parse_vector(weights)
        result = solve_knapsack(v, w, float(capacity))
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def production_ui(profit, matrix, capacities, integer):
    try:
        p = parse_vector(profit)
        A = parse_vector(matrix)
        b = parse_vector(capacities)
        result = solve_production(p, A, b, integer=integer)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def assignment_ui(costs):
    try:
        result = solve_assignment(parse_vector(costs))
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def facility_ui(fixed, capacities, demands, costs):
    try:
        result = solve_facility_location(
            parse_vector(fixed),
            parse_vector(capacities),
            parse_vector(demands),
            parse_vector(costs),
        )
        return str(result)
    except Exception as e:
        return f"Error: {e}"


with gr.Blocks(title="Integer Linear Programming Lab") as demo:
    gr.Markdown(
        """
        # Integer Linear Programming Lab

        Experiment with classical MILP models. Start small, inspect the mathematical
        formulation in the course notes, then change the data and observe the solution.
        """
    )

    with gr.Tab("Knapsack"):
        gr.Markdown("Maximize value subject to a capacity constraint. Example: `[10, 13, 17, 8]`.")
        values = gr.Textbox(value="[10, 13, 17, 8]", label="Values")
        weights = gr.Textbox(value="[5, 7, 9, 4]", label="Weights")
        capacity = gr.Number(value=15, label="Capacity")
        btn = gr.Button("Solve")
        out = gr.Textbox(label="Result")
        btn.click(knapsack_ui, [values, weights, capacity], out)

    with gr.Tab("Production"):
        gr.Markdown("Choose production quantities. Toggle integer/continuous to compare ILP with LP.")
        profit = gr.Textbox(value="[20, 30, 40]", label="Profit per unit")
        matrix = gr.Textbox(value="[[2, 3, 5], [4, 2, 3]]", label="Resource matrix")
        capacities = gr.Textbox(value="[20, 18]", label="Resource capacities")
        integer = gr.Checkbox(value=True, label="Integer variables")
        btn2 = gr.Button("Solve")
        out2 = gr.Textbox(label="Result")
        btn2.click(production_ui, [profit, matrix, capacities, integer], out2)

    with gr.Tab("Assignment"):
        costs = gr.Textbox(
            value="[[9, 2, 7], [6, 4, 3], [5, 8, 1]]",
            label="Cost matrix",
        )
        btn3 = gr.Button("Solve")
        out3 = gr.Textbox(label="Result")
        btn3.click(assignment_ui, [costs], out3)

    with gr.Tab("Facility location"):
        fixed = gr.Textbox(value="[100, 80, 120]", label="Fixed opening costs")
        caps = gr.Textbox(value="[10, 12, 15]", label="Facility capacities")
        demands = gr.Textbox(value="[5, 7, 4, 6]", label="Customer demands")
        tc = gr.Textbox(
            value="[[4, 6, 9, 7], [5, 4, 8, 6], [8, 7, 3, 5]]",
            label="Unit transport cost matrix",
        )
        btn4 = gr.Button("Solve")
        out4 = gr.Textbox(label="Result")
        btn4.click(facility_ui, [fixed, caps, demands, tc], out4)


if __name__ == "__main__":
    demo.launch()
