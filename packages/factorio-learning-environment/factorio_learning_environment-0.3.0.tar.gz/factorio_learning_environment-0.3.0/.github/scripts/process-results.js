const fs = require('fs');
const path = require('path');

const resultsDir = path.join(__dirname, '../../docs/leaderboard/results');
const outputDir = path.join(__dirname, '../../docs/leaderboard/processed');
const outputFile = path.join(outputDir, 'combined-results.json');

// Read all JSON files in the results directory
const resultFiles = fs.readdirSync(resultsDir).filter(file => file.endsWith('.json'));

// Process each file
const combinedResults = [];
resultFiles.forEach(file => {
  const filePath = path.join(resultsDir, file);
  const fileContent = fs.readFileSync(filePath, 'utf8');

  try {
    const resultData = JSON.parse(fileContent);
    
    const processedData = {
      name: resultData.name,
      productionScore: resultData.productionScore || 0,
      milestones: resultData.milestones || 0,
      automationMilestones: resultData.automationMilestones || 0,
      labTasksSuccessRate: resultData.labTasksSuccessRate || 0,
      mostComplexItem: resultData.mostComplexItem || 'none',
      submittedBy: resultData.submittedBy || 'Unknown',
      submissionDate: resultData.submissionDate || new Date().toISOString().split('T')[0],
    };

    combinedResults.push(processedData);
  } catch (error) {
    console.error(`Error processing ${file}: ${error.message}`);
  }
});

// Sort by production score
combinedResults.sort((a, b) => b.productionScore - a.productionScore);

// Write combined results to output file
fs.writeFileSync(outputFile, JSON.stringify(combinedResults, null, 2));

console.log(`Processed ${combinedResults.length} result files`);