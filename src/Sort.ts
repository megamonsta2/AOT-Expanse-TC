// Modules
import { writeFile } from "fs/promises";
import { SendErrors, FormatString, ReadFile } from "./Utils.js";
import { OUTPUT_FOLDER } from "./Constants.js";

// Variables
const INPUT_FILE = "Unsorted";
const OUTPUT_FILE = `${OUTPUT_FOLDER}/Sorted.txt`;
const REGEX_PATTERN = /[A-z0-9_]+ - ([0-9]+) \(.+\)/;
const MAX_SCORE = 100;

const SortedScores: Map<number, string[]> = new Map();

export default async () => {
  await SortScores();
  await OutputScores();
};

async function SortScores() {
  SortedScores.clear();

  const Errors: string[] = [];
  let InputData = await ReadFile(INPUT_FILE);

  while (true) {
    let AllValid = true;

    for (let index = 0; index < InputData.length; index++) {
      // Get vars
      const line = InputData[index];
      const line_number = index + 1;

      // Ignore empty strings
      if (line == "") {
        continue;
      }

      // Get parsed data
      const result = ValidateLine(line);

      // If valid, add to scores
      if (result[0]) {
        const score = result[1];
        let ScoreArray: string[];

        // Check if array exists for score
        if (SortedScores.has(score)) {
          ScoreArray = SortedScores.get(score) as string[];
        } else {
          ScoreArray = [];
          SortedScores.set(score, ScoreArray);
        }

        ScoreArray.push(line);
      } else {
        // Otherwise add to error messages
        Errors.push(FormatString(result[1], line_number, MAX_SCORE));
        AllValid = false;
      }
    }

    // Check if valid
    if (!AllValid) {
      await SendErrors("Sorted Scores", Errors);

      // Recalculate vars
      InputData = await ReadFile(INPUT_FILE);
      SortedScores.clear();
      Errors.length = 0;
    } else {
      break;
    }
  }
}

export function ValidateLine(line: string): [true, number] | [false, string] {
  const PatternResult = REGEX_PATTERN.exec(line);
  if (!PatternResult) {
    return [false, `Data on line number {0} is not valid score data.`];
  }

  const score = Number(PatternResult[1]);

  if (isNaN(score)) {
    return [false, "The score on line {0} is not a number."];
  }

  if (!Number.isInteger(score)) {
    return [false, "The score on line {0} is not an integer (whole number)."];
  }

  if (score > MAX_SCORE) {
    return [
      false,
      "The score on line {0} is greater than the maximum score ({1}).",
    ];
  }

  if (score < 0) {
    return [false, "The score on line {0} is less than 0."];
  }

  return [true, score];
}

async function OutputScores() {
  const Output: string[] = [];

  for (let i = 100; i >= 0; i--) {
    // Get scores
    const Scores = SortedScores.get(i);

    // Skip if no data
    if (!Scores) {
      continue;
    }

    // Add each score to output
    for (const line of Scores) {
      Output.push(line);
    }
  }

  await writeFile(OUTPUT_FILE, Output.join("\r\n"), "utf8");
}
