/**
 * 一键发布博客：调用 vault 根目录的 pub.sh
 * @param {Object} tp - Templater 对象，可省
 */
const { execSync } = require('child_process');
const { normalize } = require('path');

function publish(tp) {
    // 找到 Vault 绝对路径
    const vaultRoot = tp.file.folder(true).split('/').slice(0, -1).join('/'); // 去掉当前文件相对层
    const script = normalize(vaultRoot + '/pub.sh');

    try {
        // 同步执行，弹窗看结果
        const out = execSync(`"${script}"`, {
            cwd: vaultRoot,
            stdio: ['inherit', 'pipe', 'pipe'],
            encoding: 'utf8'
        });
        return `✅ 发布完成！\n${out}`;
    } catch (e) {
        return `❌ 发布失败：\n${e.stderr || e.message}`;
    }
}

module.exports = publish;