URL = ""
RECIPIENTS = [
]

// Run the createFile function to create the file and get the FILE_ID
FILE_ID = "17-uXEK22wtQALYbBhXw8UCiuJPu3ogJ1"

// Site comparison via a digest function
function md5(inputString) {
    return Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, inputString)
        .reduce((output, byte) => output + (byte < 0 ? byte + 256 : byte).toString(16).padStart(2, '0'), '');
}

function createFile() {
    var file = DriveApp.createFile("__observed_file", getSite(URL), MimeType.HTML);
    console.info("file id: %s", file.getId())
}

// Retrieves the digest file by its ID.
function getFile() {
    return DriveApp.getFileById(FILE_ID)
}

/*
 * Retrieves the content of a site.
 *
 * @param {string} url - The URL of the site to retrieve.
 * @returns {string} - The content of the site.
 */
function getSite(url) {
    var content = UrlFetchApp.fetch(url).getContentText();

    var regExp = new RegExp('<body (.|\n)+', "gi");
    return regExp.exec(content)[0]
}

/*
 * Checks a given URL for changes by comparing the current content of the site with previously saved content.
 *
 * @param {string} url - The URL of the site to check for changes.
 * @returns {boolean} - Returns true if the content has changed, false otherwise.
 */
function checkUrlForChanges(url) {
    console.log("Retrieving file")
    var file = getFile();
    var content = file.getBlob().getDataAsString();

    console.log("Retrieving site")
    var content_new = getSite(URL);

    console.log("Saving site for future comparisons")
    file.setContent(content_new)

    console.log("Performing comparison")
    var comparison = md5(content) != md5(content_new)
    return comparison
}


function test_checkUrlForChanges() {
    var file = getFile();
    var old_content = file.getBlob();
    file.setContent("")
    console.log("test_checkUrlForChanges_true: %s", checkUrlForChanges("https://www.rawelin.org/rawelin/rezerwacje-zwiedzania"))
    console.log("test_checkUrlForChanges_false: %s", checkUrlForChanges("https://www.rawelin.org/rawelin/rezerwacje-zwiedzania"))
    file.setContent(old_content)
}

// Sending the email

function sendTestEmail() {
    GmailApp.sendEmail(
        RECIPIENTS.join(","),
        "Email testowy bota sprawdzającego stronę z zapisami",
        "",
    )
}

function sendEmail(recipients) {
    console.log("Sending email")
    var now = new Date();
    GmailApp.sendEmail(
        recipients.join(","),
        "Zmiana na stronie - " + now.toString(),
        "Znalazłem zmianę na tej stronie: " + URL,
        {
            htmlBody: `Znalazłem zmianę na <a href="${URL}">tej stronie</a>.`
        }
    )
}

// Main

function main() {
    if (checkUrlForChanges(URL)) {
        console.log("Changes found")
        sendEmail(RECIPIENTS)
    } else {
        console.log("No changes found")
    }
}
