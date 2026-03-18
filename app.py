function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("LuminaSoul_Data");
    var data = JSON.parse(e.postData.contents);

    sheet.appendRow([
      new Date(),                    // A วัน/เวลา
      data.name || "",               // B ชื่อ
      data.line_id || "",            // C ID Line
      data.birthdate || "",          // D วันเกิด
      data.category || "",           // E หมวดหมู่
      data.question || "",           // F คำถาม/ปัญหา
      data.result || "",             // G ข้อที่ได้รับ
      data.strength || "",           // H จุดเด่นพลังงาน
      data.next_step || "",          // I แนวทางถัดไป
      data.caution || "",            // J สิ่งที่ควรระวัง
      data.language || "",           // K ภาษา
      data.source || "",             // L แหล่งที่มา
      data.submitted_at || ""        // M submitted_at
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: "success" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({
        status: "error",
        message: error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
