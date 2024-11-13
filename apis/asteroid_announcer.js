function get_asteroid_data() {
    const current_date = Utilities.formatDate(new Date(), "GMT+1", "yyyy-MM-dd")
    const response = UrlFetchApp.fetch(`https://api.nasa.gov/neo/rest/v1/feed?start_date=${current_date}&end_date=${current_date}&api_key=DEMO_KEY`)
    return JSON.parse(response.getContentText())["near_earth_objects"][current_date]
}
  
function send_mail(content) {
    GmailApp.sendEmail(
        "wahefil142@gianes.com",
        "Asteroidy dzisiaj",
        content
    )
}

function main() {
    const astro_data = get_asteroid_data()
    console.log(astro_data)
    send_mail(
        astro_data.map(entry => {
        return `${entry['name']}, szeroki na ${entry['estimated_diameter']['meters']['estimated_diameter_max']} metrów. ${entry['nasa_jpl_url']}`
        }).join("\n")
    )
}
  
  