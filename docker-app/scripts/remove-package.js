#!/usr/bin/env node

const { execSync } = require('child_process');
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: npm run remove-package <package-name>');
    console.log('Examples:');
    console.log('  npm run remove-package requests');
    console.log('  npm run remove-package django');
    process.exit(1);
}

const packageName = args.join(' ');

try {
    console.log(`Removing ${packageName}...`);

    // Remove the package
    execSync(`docker-compose run --rm dev pip uninstall -y ${packageName}`, {
        stdio: 'inherit'
    });

    // Update requirements.txt
    execSync('docker-compose run --rm dev pip freeze > requirements.txt', {
        stdio: 'inherit'
    });

    console.log(`${packageName} removed and requirements.txt updated!`);
} catch (error) {
    console.error('Error removing package:', error.message);
    process.exit(1);
}