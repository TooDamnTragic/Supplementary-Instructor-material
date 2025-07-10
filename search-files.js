const fs = require('fs');
const path = require('path');

// Function to recursively find files with specific extension
function findFiles(dir, extension) {
  const files = [];
  
  try {
    const items = fs.readdirSync(dir);
    
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      
      if (stat.isDirectory()) {
        files.push(...findFiles(fullPath, extension));
      } else if (stat.isFile() && item.endsWith(extension)) {
        files.push(fullPath);
      }
    }
  } catch (error) {
    // Directory might not exist or be accessible
    console.error(`Error reading directory ${dir}:`, error.message);
  }
  
  return files;
}

// Function to search for patterns in file content
function searchInFile(filePath, patterns) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const regex = new RegExp(patterns.join('|'), 'i');
    return regex.test(content);
  } catch (error) {
    console.error(`Error reading file ${filePath}:`, error.message);
    return false;
  }
}

// Main execution
const searchDir = 'GCIS124'; // Fixed directory name
const fileExtension = '.py';
const searchPatterns = [
  'CTF',
  'hackathon',
  'steghide',
  'brute.*force',
  'chess.*flag',
  'MetaCTF',
  'crypto.*challenge',
  'password.*crack'
];

console.log(`Searching for Python files in ${searchDir} directory...`);

const pythonFiles = findFiles(searchDir, fileExtension);
console.log(`Found ${pythonFiles.length} Python files`);

const matchingFiles = [];
for (const file of pythonFiles) {
  if (searchInFile(file, searchPatterns)) {
    matchingFiles.push(file);
  }
}

if (matchingFiles.length > 0) {
  console.log('\nFiles containing the search patterns:');
  matchingFiles.forEach(file => console.log(file));
} else {
  console.log('\nNo files found containing the search patterns.');
}