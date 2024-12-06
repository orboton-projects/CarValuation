const { devices } = require('@playwright/test');

module.exports = {
  browsers: ['chromium'],
  use: {
    headless: true, // Run tests in headless mode
    trace: 'on',    // Collect trace data
  },
  outputDir: 'test-results/', // Save test results
};
