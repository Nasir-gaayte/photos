# photos
       <form class=" card" method="POST" enctype="multipart/form-data">
                            <div class="form-group m-3">
                                <label >Description</label> 
                                <input name="description" type="text" placeholder="Add your descriptions">
                            </div>
                            <div class="form-group m-3">
                                <label >Select Category</label>
                                <select class="form-control" name="catehory">
                                    <option value="none">Select a category...</option>
                                    {% for cat in cats %}
                                    <option value="{{cat.id}}">{{cat.name}}</option>
                                    {% endfor %}
                                </select>
                            </div>
                            <div class="form-group m3">
                                <label >Creat New Category</label>
                                <input name="category_new" type="text"  placeholder="add category" class="form-control-file">
                            </div>

                            <div class="form-group m3">
                                <label >Upload image</label>
                                <input name="image" type="file" class="form-control-file">
                            </div>
                            <button class="btn btn-dark btn-block" type="submit">ADD</button>
                        </form>