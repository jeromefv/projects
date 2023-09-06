# csv files in directory
csv_target = "edits_standard_url.csv"
pathway = "edits_standard.csv"

# Regex
regex_group = [   
            ["\n\n*\n", "\n\n"], # Multiple new lines in file
            "^\n\n*\n", # At front of file
            "$\n\n*\n", # At end of file
            ["\\\_", "_"], # Broken underscores
            "Â", # Unsupported characters
            "â",
            "",
            "  " # Double spaces
]

# Path structure
root = "./doc_test"
markdown = ".md"
