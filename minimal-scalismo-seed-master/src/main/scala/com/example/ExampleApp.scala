package com.example

import java.io.File

import scalismo.geometry._3D
import scalismo.ui.api.ScalismoUI

object LandmarkClickExample extends App {

  /*1. Open the BFM*/

  val model = scalismo.faces.io.MoMoIO.read(new File("/home/hao/lepere/basel/model2017-1_bfm_nomouth.h5")).get

  val referenceTemplate = model.neutralModel.referenceMesh

  val ui = ScalismoUI()

  ui.show(referenceTemplate,"Template")

  /* 2. Now a UI opens and you can click landmarks on the template and give them names ...
  *
  * You can save the landmarks as JSON or CSV within the UI
  *
  * For instance: ibug.json
  *
  * */

  /*3. Then you can load the landmarks in the following way:*/

  //val lms = scalismo.io.LandmarkIO.readLandmarksJson[_3D](new File("PATH_TO_ibug.json")).get

  /*4. You can put them back into the model: */

  //val newModelWithLandmarks = model.withLandmarks(lms.map(f => (f.id -> f)).toMap)

  /*5. And save them again: */

  //scalismo.faces.io.MoMoIO.write(newModelWithLandmarks,new File("PATH_TO_UPDATED_MODEL"))

}
