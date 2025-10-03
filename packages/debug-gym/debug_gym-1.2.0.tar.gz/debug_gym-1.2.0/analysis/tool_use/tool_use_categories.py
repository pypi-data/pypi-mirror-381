import argparse
import glob
import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm

plt.rcParams.update(
    {
        "font.size": 22,  # Base font size
        "axes.labelsize": 22,  # Axis labels
        "axes.titlesize": 22,  # Plot title
        "xtick.labelsize": 22,  # X-axis tick labels
        "ytick.labelsize": 22,  # Y-axis tick labels
        "legend.fontsize": 22,  # Legend text
    }
)


def analyze_froggy_results(model_name):
    """
    Analyzes froggy.jsonl files for a given model to extract success rates and rewrite counts.
    Args:
        model_name (str): Path to the model directory (e.g. 'exps/swe-bench/rewrite_4o_0')

    Returns:
        pd.DataFrame: DataFrame containing results by task
    """
    model_dir = os.path.join(model_name)
    results = []

    for jsonl_name in ["debug_gym.jsonl"]:
        for jsonl_file in glob.glob(f"{model_dir}/**/{jsonl_name}", recursive=True):
            # Get task name from directory path
            task = os.path.dirname(jsonl_file).split("/")[-1]
            # import pdb; pdb.set_trace()

            with open(jsonl_file) as f:
                data = json.load(f)

                # Extract success status
                success = data.get("success", False)

                # Count rewrite commands
                episode_length = 0

                tool_counter = {
                    "view": 0,
                    "listdir": 0,
                    "pdb": 0,
                    "rewrite": 0,
                    "eval": 0,
                    "other": 0,
                }

                for step in data.get("log", []):
                    episode_length += 1
                    if step.get("action") is None:
                        continue
                    tool_name = step["action"]["name"]
                    if tool_name in tool_counter:
                        tool_counter[tool_name] += 1
                    else:
                        tool_counter["other"] += 1

                results.append(
                    {
                        "task": task,
                        "success": success,
                        "episode_length": episode_length,
                        "tool_counter": tool_counter,
                    }
                )

    df = pd.DataFrame(results)
    return df


def analyze_froggy_results_with_seeds(base_model_name, seeds=[0, 1, 2]):
    """
    Analyzes and averages results across different seeds for a base model name

    Args:
        base_model_name (str): Base path without seed (e.g. '../exps/may22/rewrite_o3-mini')
        seeds (list): List of seeds to average over

    Returns:
        pd.DataFrame: DataFrame containing averaged results by task
    """
    all_dfs = []

    for seed in seeds:
        model_path = f"{base_model_name}_{seed}"
        try:
            df = analyze_froggy_results(model_path)
        except:
            continue
        df["seed"] = seed
        all_dfs.append(df)

    # Combine all DataFrames
    combined_df = pd.concat(all_dfs)

    return combined_df


def plot_tool_use_categories(df_dict, model_paths, figsize=(12, 7)):
    """
    Creates a grouped hist plot showing the distribution of tool use categories for each model.
    Args:
        df_dict (dict): Dictionary mapping model names to their DataFrames with averaged results
        model_paths (list): List of model paths for custom x-tick labels
        figsize (tuple): Figure size (width, height)
    """

    all_data = []
    # Create plot for each model
    for model_name, df in df_dict.items():
        # o1, o3-mini, o1, o3-mini, o1, o3-mini
        tool_category_per_model = {
            "view": 0,
            "listdir": 0,
            "pdb": 0,
            "rewrite": 0,
            "eval": 0,
            "other": 0,
        }
        tool_call_count = 0
        for _kv in df["tool_counter"].items():
            if _kv[1] == {}:
                continue
            for k, v in _kv[1].items():
                tool_call_count += v
                tool_category_per_model[k] += v
        # percentage
        tool_category_per_model = {
            k: round(v / tool_call_count, 2) for k, v in tool_category_per_model.items()
        }
        all_data.append(
            [
                model_name,
                model_name.split("_")[1],
                tool_category_per_model["view"],
                tool_category_per_model["listdir"],
                tool_category_per_model["pdb"],
                tool_category_per_model["rewrite"],
                tool_category_per_model["eval"],
                tool_category_per_model["other"],
            ]
        )
    print(all_data)
    # convert to DataFrame
    all_data = pd.DataFrame(
        all_data,
        columns=["name", "model", "view", "listdir", "pdb", "rewrite", "eval", "other"],
    )
    # nice palette
    palette = sns.color_palette("Set2")
    # set color
    sns.set_palette(palette)
    # stacked bar plot showing the distribution of PDB command categories for each model
    all_data.set_index("name")[
        ["view", "listdir", "pdb", "rewrite", "eval", "other"]
    ].plot(kind="bar", stacked=True, figsize=figsize)
    plt.xlabel("Backbone LLM")
    plt.ylabel("Percentage")
    plt.xticks(rotation=90)
    # custom x ticks
    plt.xticks(
        np.arange(len(all_data)),
        [
            item.split("/")[-1].replace("rewrite_", "rw ").replace("debug_", "dbg ")
            for item in model_paths
        ],
    )

    plt.tight_layout()
    plt.show()


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Filter trajectory files based on specified criteria"
    )
    parser.add_argument(
        "--exp-path",
        required=True,
        help="Path to experiments directory, e.g., '../../exps/'",
    )
    parser.add_argument(
        "--exp-uuid-list",
        nargs="+",  # Accept one or more arguments
        required=True,
        help="A list of experiment UUID/name to analyze, e.g., exp1 exp2 exp3",
    )

    args = parser.parse_args()
    model_paths = [os.path.join(args.exp_path, item) for item in args.exp_uuid_list]

    # Analyze all models with seed averaging
    results_dict = {}
    for _path in tqdm(model_paths):
        _name = _path.split("/")[-1]
        results_dict[_name] = analyze_froggy_results_with_seeds(_path, seeds=[0])

    # Plot comparison
    plot_tool_use_categories(results_dict, model_paths)


if __name__ == "__main__":
    main()
