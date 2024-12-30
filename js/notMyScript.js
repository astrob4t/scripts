// Import modules
const fs = require('fs');
const path = require('path');

// Edit these vv
const chart_path = "C:/Users/abelf/AppData/Roaming/beatblock/Custom Levels/My Levels/WIP/anybody can find love (except you.)"; // Path to LEVEL FOLDER
const beat_start = 0;          // What beat to start spawning blocks
const block_count = 50;         // How many blocks to spawn
const block_space = 1;         // How many beats between each block
const block_rotation = 90;     // The rotation of each block

try {
    // Get chart data
    const chart_dat_path = path.join(chart_path, 'chart-anybody (except you.).json');
    let chart_dat = JSON.parse(fs.readFileSync(chart_dat_path, 'utf8'));

    // Create a backup file if it doesn't exist
    const backup_path = path.join(chart_path, 'chart-backup.json');
    if (!fs.existsSync(backup_path)) {
        fs.writeFileSync(backup_path, JSON.stringify(chart_dat, null, 2), 'utf8');
    } else {
        console.log('Backup already exists. Using backup...');
        chart_dat = JSON.parse(fs.readFileSync(backup_path, 'utf8'));
    }

    // Start spawning blocks
    for (let i = 0; i < block_count; i++) {
        const current_beat = i * block_space + beat_start;
        chart_dat.push({
            type: 'block',
            time: current_beat,
            angle: block_rotation,
        });
    }

    // Save chart
    fs.writeFileSync(chart_dat_path, JSON.stringify(chart_dat, null, 2), 'utf8');
    console.log('Chart updated :D');
} catch (error) {
    console.error('Error updating chart:', error);
}

// Made by LemonadeVR, I still need to learn JS