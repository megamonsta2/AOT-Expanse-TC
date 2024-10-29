// Modules
import { Practical, AddScores } from "./Storage.js";

// Variables
const MAX_SCORES: { [key in Practical]: number } = {
  Dummies: 0,
  Speed: 15,
  Musket: 5,
};
export const MAX_SCORE = (MAX_SCORES.Musket + MAX_SCORES.Speed) * 2;

// Module Setup
export default async () => {
  await Promise.all([
    GetScores("Musket"),
    GetScores("Speed"),
    GetScores("Dummies"),
  ]);
};

async function GetScores(prac: Practical) {
  await AddScores(prac, prac, MAX_SCORES[prac], (player, score: number) => {
    player.AddCorePractical(prac, score);
  });
}
