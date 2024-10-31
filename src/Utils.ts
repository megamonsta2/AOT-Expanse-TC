import { createInterface } from "readline";
import { readFile } from "fs/promises";
import { INPUT_FOLDER } from "./Constants.js";

export async function SendErrors(type: string, Errors: string[]) {
  // Display error messages
  console.warn(`These are the errors for the ${type} input.`);
  Errors.forEach((msg: string) => console.warn(msg));

  // Wait for input
  console.warn("When the errors are amended, press any key.");
  await WaitForKey();
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

export function FormatString(
  format: string,
  ...args: (string | number)[]
): string {
  return format.replace(/\{(\d+)\}/g, (match, index) => {
    const idx = parseInt(index, 10);
    return args[idx] !== undefined ? String(args[idx]) : match;
  });
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
