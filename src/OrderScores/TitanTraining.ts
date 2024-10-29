// Modules
import { AddScores } from "./Storage.js";

// Variables
const MAX_SCORE = 40;

// Module Setup
export default async () => {
  await AddScores(
    "Titan Training",
    "TitanTraining",
    MAX_SCORE,
    (player, score: number) => {
      player.AddTitanTraining(score);
    },
  );
};
