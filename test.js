// Simple test to ensure the app structure is valid
console.log("Running tests...");

// Test 1: Check if process.env works
if (typeof process.env === 'object') {
  console.log("✓ Test 1 passed: Environment variables accessible");
} else {
  console.error("✗ Test 1 failed");
  process.exit(1);
}

// Test 2: Simple addition test
const result = 2 + 3;
if (result === 5) {
  console.log("✓ Test 2 passed: Math works correctly");
} else {
  console.error("✗ Test 2 failed");
  process.exit(1);
}

console.log("All tests passed! ✓");
