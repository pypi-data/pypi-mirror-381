from ..imports import *
from flask import Response

def send_via_nginx(abs_path: str, filename: str):
    """
    Return a response telling Nginx to serve the file directly.
    """
    rel_path = str(abs_path).split("/24T/media/")[-1]  # adjust to your base
    resp = Response()
    resp.headers["Content-Type"] = "application/octet-stream"
    resp.headers["Content-Disposition"] = f'attachment; filename="{filename}"'
    resp.headers["X-Accel-Redirect"] = f"/protected/{rel_path}"
    return resp
secure_download_bp, logger = get_bp(
    "secure_download",
    __name__
)

@secure_download_bp.route("/api/secure-files/download", methods=['GET',"POST"])
@login_required
def downloadFile():
    #initialize_call_log()
    
    args,datas,username = get_args_jwargs_user_req(request)
    logger.info(datas)
            # Validate and collect files
    valid_files = []
    errors = []
    for i,data in enumerate(make_list(datas)):
        data = dict(data)
        abs_path=None
        filename = None
        err = False
        filepath = data.get('filepath')
        if filepath:
          abs_path,filename = get_path_and_filename(filepath)
        filename = data.get('filename')
        
        logger.info(f"dict dsata =={data}")
        if not filename or not abs_path:
           abs_path, filename, err = get_download(
              data=data,
              username=username
              )
        logger.info(f"abs_path =={filepath}")
        logger.info(f"err =={err}")
        logger.info(f"filename =={filename}")
        
        if err:
            errors.append((filename, err))
            continue
        if isinstance(filename, int):
            errors.append((filename, 'Invalid filename'))
            continue
        valid_files.append((abs_path, filename))

    if len(valid_files) >1:
        # safety-check – abs_path/filename should never be None here
        if not abs_path or not filename:
            return get_json_call_response({"error": "NO_FILE_FOUND"}, 404)
                # Create ZIP archive in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for abs_path, filename in valid_files:
                    # Ensure unique filenames in ZIP (handle duplicates)
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    unique_filename = filename
                    while unique_filename in [f[1] for f in valid_files[:len(valid_files)-1]]:
                        unique_filename = f"{base}_{counter}{ext}"
                        counter += 1
                    zip_file.write(abs_path, unique_filename)
                    logger.info(f"Added {filename} to ZIP as {unique_filename}")

            zip_buffer.seek(0)

            # Log partial errors if any
            if errors:
                error_msg = '; '.join([f"{fid}: {err}" for fid, err in errors])
                logger.warning(f"Partial success: {error_msg}")

        # Send ZIP file
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name='downloads.zip',
            mimetype='application/zip'
        )
    else:
        return send_file(
            abs_path,
            as_attachment=True,
            download_name=filename      # now includes extension – MIME will resolve
        )


@secure_download_bp.route('/api/secure-files/secure-download', methods=['POST'])
@secure_download_bp.route('/api/secure-files/secure-download/', methods=['POST'])
@secure_download_bp.route('/api/secure-files/secure-download/<int:id>', methods=['GET','POST'])
@secure_download_bp.route('/api/secure-files/secure-download/<int:id>/<string:pwd>', methods=['GET','POST'])
def download_file(id: int=None,pwd:str =None):
    initialize_call_log()
    search_map,data,row = get_searchmap_data_row(req=request)
 
    abs_path, filename, err = get_download(req=request,
                                           data=data,
                                           search_map=search_map,
                                           row=row
                                           )
    is_user = is_user_uploader(req=request, data=data)

    # handle missing file or other checks
    if err == 'NO_FILE_FOUND':
        return get_json_call_response('No file found.', 404)
    if not is_user and err == 'NOT_SHAREABLE':
        return get_json_call_response('Not shareable', 403)
    if not is_user and err == 'DOWNLOAD_LIMIT':
        return get_json_call_response('download limit reached', 403)
    logger.info(f"abs_path = {abs_path}\nfilename = {filename}\nsearch_map = {search_map}\nerr = {err}\n data = {data}")
    # Password flow
    share_password = getRowValue(
       
        req=request,
        data=data,
        search_map=search_map,
        row=row,
        key='share_password'
        )
    
    file_id = data.get('id')
    if not is_user and err in ('PASSWORD_REQUIRED', 'PASSWORD_INCORRECT'):
          return render_template(
              'enter_password.html',
              file_id=file_id,
              error='Incorrect password.' if err == 'PASSWORD_INCORRECT' else None
          ), 401
    # increment count (non-owner)
    if not is_user:
        add_to_download_count(search_map)
        

    # owners or password-valid → send
    return send_via_nginx(abs_path, filename)

    # Handle multiple file download (POST request)
    if request.method == 'POST':
        # Get file_ids from JSON payload or form data
        file_ids = data.get('file_ids', [])
        
        logger.info(f"abs_path, filename, err == {abs_path} {filename} {err}")

        
        if not file_ids:
           if 'file_ids' in request.form:
               file_ids = request.form['file_ids'].split(',')
           else:
               return get_json_call_response('No file_ids provided.', 400)

        if not file_ids:
            return get_json_call_response('No files specified.', 400)

        logger.info(f"Multiple file download requested: file_ids={file_ids}")

        # Validate and collect files
        valid_files = []
        errors = []
        for fid in file_ids:
            abs_path, filename, err = get_download(request)
            if err:
                errors.append((filename, err))
                continue
            if isinstance(filename, int):
                errors.append((filename, 'Invalid filename'))
                continue
            valid_files.append((abs_path, filename))

        # Handle errors
        if not valid_files and errors:
            error_msg = '; '.join([f"{fid}: {err}" for fid, err in errors])
            return get_json_call_response(f"Failed to download files: {error_msg}", 403)

        # Create ZIP archive in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for abs_path, filename in valid_files:
                # Ensure unique filenames in ZIP (handle duplicates)
                base, ext = os.path.splitext(filename)
                counter = 1
                unique_filename = filename
                while unique_filename in [f[1] for f in valid_files[:len(valid_files)-1]]:
                    unique_filename = f"{base}_{counter}{ext}"
                    counter += 1
                zip_file.write(abs_path, unique_filename)
                logger.info(f"Added {filename} to ZIP as {unique_filename}")

        zip_buffer.seek(0)

        # Log partial errors if any
        if errors:
            error_msg = '; '.join([f"{filename}: {err}" for fid, err in errors])
            logger.warning(f"Partial success: {error_msg}")

        # Send ZIP file
        zip_buffer.seek(0)
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name='downloads.zip',
            mimetype='application/zip'
        )

@secure_download_bp.route("/api/secure-files/secure-download/token/<token>")
@secure_limiter.limit("10000 per hour")
@login_required
def download_with_token(token):
    initialize_call_log()
    try:
        data = decode_token(token)
    except jwt.ExpiredSignatureError:
        return get_json_call_response("Download link expired.", 410)
    except jwt.InvalidTokenError:
        return get_json_call_response("Invalid download link.", 400)
    # Check that the token’s user matches the logged-in user
    if data["sub"] != get_user_name(request):
        return get_json_call_response("Unauthorized.", 403)
    # Then serve exactly like before, using data["path"]
    return _serve_file(data["path"])


