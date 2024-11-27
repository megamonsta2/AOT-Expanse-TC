// Modules
import { LogPlayer, ValidateLine } from "./Storage.js";
import { ReadFile, WaitForKey, FormatString, SendErrors } from "../Utils.js";

// Variables
const MAX_SCORE = 60;

// Module Setup
export default async () => {
  const [RawNames, RawScores] = await GetData();
  LogPlayers(RawNames, RawScores);
};

async function GetData() {
  let [RawNames, RawScores] = await ReadFiles();
  const ErrorMessages: string[] = [];

  // Check lengths
  while (!(RawNames.length == RawScores.length)) {
    console.warn(
      "The length of the knowledge test names and scores are NOT the same.\r\nWhen this is amended, press any key.",
    );
    await WaitForKey();

    [RawNames, RawScores] = await ReadFiles();
  }

  while (true) {
    let AllValid = true;

    for (let index = 0; index < RawNames.length; index++) {
      // Get vars
      const line = `${RawNames[index].trim()} - ${RawScores[index].trim()}`;
      const line_number = index + 1;

      // Get parsed data
      const result = ValidateLine(line, MAX_SCORE);

      // If valid, add to scores
      if (!result[0]) {
        // Otherwise add to error messages
        ErrorMessages.push(FormatString(result[1], line_number, MAX_SCORE));
        AllValid = false;
      }
    }

    // Check if valid
    if (!AllValid) {
      await SendErrors("knowledge", ErrorMessages);

      // Recalculate vars
      RawScores = await ReadFile("KnowledgeScores");
      ErrorMessages.length = 0;
    } else {
      break;
    }
  }

  return [RawNames, RawScores];
}

function ReadFiles(): Promise<string[][]> {
  return Promise.all([ReadFile("KnowledgeNames"), ReadFile("KnowledgeScores")]);
}

function LogPlayers(RawNames: string[], RawScores: string[]) {
  for (let i = 0; i < RawNames.length; i++) {
    const name = RawNames[i].trim();
    const score = Number(RawScores[i].trim());

    LogPlayer({ Name: name, Score: score }, (player, score: number) => {
      player.AddKnowledge(score);
    });
  }
}
