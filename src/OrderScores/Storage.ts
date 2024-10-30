// Modules
import { createInterface } from "readline";
import { readFile } from "fs/promises";
import { INPUT_FOLDER } from "../Constants.js";

// Types
export type Practical = "Musket" | "Speed" | "Dummies";
type RawScore = { Name: string; Score: number };

// Variables
const Players: Map<string, Player> = new Map<string, Player>();
const Missing: Map<string, Player> = new Map<string, Player>();

const FORMAT = "USERNAME - PATTERN";
const REGEX_PATTERN = /([A-z0-9_]+) - ([0-9]+)/;

// Player
export class Player {
  Username: string;

  Knowledge!: number;
  BonusPoints!: number;

  Musket!: number;
  Speed!: number;
  Dummies!: number;
  TitanTraining!: number;
  HasPractical: boolean;

  constructor(Username: string) {
    this.Username = Username;
    this.HasPractical = false;
  }

  AddKnowledge(score: number) {
    // If knowledge doesn't exist or exists and score is less than current knowledge
    if (!this.Knowledge || this.Knowledge > score) {
      this.Knowledge = score;
    }
  }

  AddBonusPoints(points: number, max: number) {
    if (!this.BonusPoints) {
      this.BonusPoints = 0;
    }

    if (this.BonusPoints + points <= max) {
      this.BonusPoints += points;
    } else {
      this.BonusPoints = max;
    }
  }

  AddCorePractical(type: Practical, score: number) {
    score *= 2;

    // If prac score doesn't exist or exists and score is less than current prac
    if (!this[type] || this[type] > score) {
      this[type] = score;

      this.HasPractical = true;
    }
  }

  AddTitanTraining(score: number) {
    // Must not have other prac scores
    if (this.HasPractical) {
      return;
    }

    // If tt score doesn't exist or exists and score is greater than current tt score
    if (!this.TitanTraining || score > this.TitanTraining) {
      this.TitanTraining = score;
    }
  }
}

export function GetPlayers() {
  return Players;
}

function GetPlayer(username: string): Player | undefined {
  return Players.get(GetId(username));
}

export function AddPlayer(username: string) {
  Players.set(GetId(username), new Player(username));
}

export function GetMissingPlayers() {
  return Missing;
}

function GetMissingPlayer(username: string): Player | undefined {
  return Missing.get(GetId(username));
}

function AddMissingPlayer(username: string): Player {
  const MissingPlayer = new Player(username);
  Missing.set(GetId(username), MissingPlayer);
  return MissingPlayer;
}

export function RemoveMissingPlayer(username: string) {
  Missing.delete(GetId(username));
}

export function ResetPlayers() {
  Players.clear();
  Missing.clear();
}

function GetId(username: string): string {
  return username.toLowerCase();
}

// Score Functions
export async function AddScores(
  type: string,
  file: string,
  max: number,
  func: (player: Player, score: number) => void,
) {
  const Scores = await GetScores(type, file, max);
  const Promises: Promise<void>[] = [];

  for (let i = 0; i < Scores.length; i++) {
    LogPlayer(Scores[i], func);
  }

  return Promise.all(Promises);
}

async function GetScores(type: string, file: string, max: number) {
  let CurrentInput = await ReadFile(file);
  const Scores: RawScore[] = [];
  const ErrorMessages: string[] = [];

  // Check if scores are valid
  while (true) {
    let AllValid = true;

    for (let index = 0; index < CurrentInput.length; index++) {
      // Get vars
      const line = CurrentInput[index];
      const line_number = index + 1;

      // Ignore empty strings
      if (line == "") {
        continue;
      }

      // Get parsed data
      const result = ValidateLine(line, max);

      // If valid, add to scores
      if (result[0]) {
        Scores.push({ Name: result[1], Score: result[2] });
      } else {
        // Otherwise add to error messages
        ErrorMessages.push(FormatString(result[1], line_number, max));
        AllValid = false;
      }
    }

    // Check if valid
    if (!AllValid) {
      await SendErrors(type, ErrorMessages);

      // Recalculate vars
      CurrentInput = await ReadFile(file);
      Scores.length = 0;
      ErrorMessages.length = 0;
    } else {
      break;
    }
  }

  return Scores;
}

export function ValidateLine(
  line: string,
  max: number,
): [true, string, number] | [false, string] {
  const PatternResult = REGEX_PATTERN.exec(line);
  if (!PatternResult) {
    return [
      false,
      `Data on line number {0} does not match the format ${FORMAT}.`,
    ];
  }

  const name = PatternResult[1];
  const score = Number(PatternResult[2]);

  if (isNaN(score)) {
    return [false, "The score on line {0} is not a number."];
  }

  if (!Number.isInteger(score)) {
    return [false, "The score on line {0} is not an integer (whole number)."];
  }

  if (score > max) {
    return [
      false,
      "The score on line {0} is greater than the maximum score ({1}).",
    ];
  }

  if (score < 0) {
    return [false, "The score on line {0} is less than 0."];
  }

  return [true, name, score];
}

export function LogPlayer(
  Score: RawScore,
  func: (player: Player, score: number) => void,
) {
  const name = Score.Name;
  const score = Score.Score;

  // Check if player is AT
  const player = GetPlayer(name);
  if (player) {
    // Player exists as AT
    func(player, score);
    return;
  }

  // Check if has missing data
  let MissingPlayer = GetMissingPlayer(name);
  if (!MissingPlayer) {
    MissingPlayer = AddMissingPlayer(name);
  }

  // Run func
  func(MissingPlayer, score);
}

// Other Functions
export async function SendErrors(type: string, Errors: string[]) {
  // Display error messages
  console.warn(`These are the errors for the ${type} input.`);
  Errors.forEach((msg: string) => console.warn(msg));

  // Wait for input
  console.warn("When the errors are amended, press any key.");
  await WaitForKey();
}

export async function ReadFile(file: string): Promise<string[]> {
  const data = (await readFile(`${INPUT_FOLDER}/${file}.txt`, "utf8")).split(
    "\r\n",
  );

  // Is empty table with 1 empty string
  if (data.length == 1 && data[0] == "") {
    return [];
  } else {
    return data;
  }
}

export function FormatString(
  format: string,
  ...args: (string | number)[]
): string {
  return format.replace(/\{(\d+)\}/g, (match, index) => {
    const idx = parseInt(index, 10);
    return args[idx] !== undefined ? String(args[idx]) : match;
  });
}

export function WaitForKey(): Promise<void> {
  return new Promise((resolve) => {
    // Get interface
    const rl = createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    // Once a key is pressed, close then resolve
    process.stdin.once("data", () => {
      rl.close();
      resolve();
    });
  });
}
