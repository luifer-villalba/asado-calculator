function isMobile() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}
window.addEventListener('DOMContentLoaded', function() {
    if (isMobile()) {
        document.getElementById('share-container').style.display = 'block';
    }
    const shareBtn = document.getElementById('share-btn');
    if (shareBtn) {
        shareBtn.onclick = function() {
            const text = document.getElementById('share-text').value;
            if (navigator.share) {
                navigator.share({
                    title: 'Cálculo de Asado',
                    text: text
                });
            } else {
                navigator.clipboard.writeText(text).then(function() {
                    document.getElementById('share-msg').style.display = 'inline';
                    setTimeout(() => {
                        document.getElementById('share-msg').style.display = 'none';
                    }, 2000);
                });
            }
        }
    }
});