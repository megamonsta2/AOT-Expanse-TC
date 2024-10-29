// Modules
import { ResetPlayers } from "./Storage.js";
import GetUsernames from "./Usernames.js";
import GetKnowledge from "./Knowledge.js";
import GetPractical from "./Practical.js";
import GetTitanTraining from "./TitanTraining.js";
import GetBonusPoints from "./BonusPoints.js";
import Validate from "./Validate.js";
import Output from "./Output.js";

// Module Setup
export async function index() {
  ResetPlayers();

  await GetUsernames();
  console.log("Gotten usernames.");
  await GetKnowledge();
  console.log("Gotten knowledge scores.");
  await GetPractical();
  console.log("Gotten practical scores.");
  await GetTitanTraining();
  console.log("Gotten titan training scores.");
  await GetBonusPoints();
  console.log("Gotten bonus points.");

  await Validate();
  await Output();
}
